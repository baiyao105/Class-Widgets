"""
ui加载中间层

*没有什么是不能通过增加一个中间层来解决的(
"""

import importlib.util
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import lru_cache
from pathlib import Path
from typing import List, Optional, Tuple, Union

from loguru import logger
from PySide6 import QtCore, QtUiTools
from PySide6.QtWidgets import QWidget

import resources_rc  # noqa: F401
from basic_dirs import CW_HOME


class UiLoadError(Exception):
    """.ui 加载失败"""

    def __init__(self, ui_path: Path, message: str):
        self.ui_path = ui_path
        super().__init__(f"加载 .ui 文件 {ui_path} 失败: {message}")


class UiLoader:
    """
    .ui加载类
    """

    @staticmethod
    @lru_cache(maxsize=128)
    def get_py_path_from_ui_path(ui_path: Union[str, Path]) -> Optional[Path]:
        """
        路径转换

        1. view/**/*.ui -> view/py/**/*.py
        2. ui/xxx/*.ui -> ui/xxx/py/*.py
        3. ui/xxx/dark/*.ui -> ui/xxx/dark/py/*.py
        """
        ui_path = Path(ui_path)
        try:
            rel_ui_path = ui_path.relative_to(CW_HOME) if ui_path.is_absolute() else ui_path
        except ValueError:
            logger.error(f"路径无法相对化: {ui_path}")
            return None

        parts = rel_ui_path.parts
        if not parts:
            return None
        if parts[0] == "view":
            return CW_HOME / Path("view", "py", *parts[1:]).with_suffix(".py")
        if parts[0] == "ui" and len(parts) >= 2:
            theme_name = parts[1]
            if len(parts) >= 3 and parts[2] == "dark":
                return CW_HOME / Path("ui", theme_name, "dark", "py", *parts[3:]).with_suffix(".py")
            return CW_HOME / Path("ui", theme_name, "py", *parts[2:]).with_suffix(".py")
        logger.warning(f"无效的 ui 路径: {ui_path}")
        return None

    @staticmethod
    def _load_ui_module(py_file: Path) -> Optional[object]:
        """加载 .py 文件为模块"""
        try:
            rel_path = py_file.relative_to(CW_HOME)
            module_name = f"ui_{rel_path.stem}_{rel_path.parent.as_posix().replace('/', '_')}"
            spec = importlib.util.spec_from_file_location(module_name, py_file)
            if spec is None or spec.loader is None:
                logger.error(f"无法创建模块规范: {py_file}")
                return None
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            return module
        except Exception as e:
            logger.error(f"加载模块失败: {py_file} - {e}")
            return None
        finally:
            if module_name in sys.modules:
                del sys.modules[module_name]  # 清理模块缓存

    @staticmethod
    def load_py_ui(py_file: Path, widget: QWidget) -> bool:
        """
        加载.py文件到widget
        """
        with logger.contextualize(py_file=str(py_file)):
            module = UiLoader._load_ui_module(py_file)
            if not module:
                return False
            try:
                ui_class = next(
                    (
                        getattr(module, attr)
                        for attr in dir(module)
                        if isinstance((attr_val := getattr(module, attr)), type)
                        and attr.startswith("Ui_")
                        and hasattr(attr_val, "setupUi")
                    ),
                    None,
                )
                if not ui_class:
                    logger.error(f"未找到 Ui_ 类: {py_file}")
                    return False
                ui_instance = ui_class()
                ui_instance.setupUi(widget)
                if hasattr(ui_instance, "retranslateUi"):
                    ui_instance.retranslateUi(widget)
                widget.ui = ui_instance  # type: ignore[attr-defined]
                return True
            except Exception as e:
                logger.error(f"设置 .ui 失败: {py_file} - {e}")
                return False

    @staticmethod
    def load_ui(ui_path: Union[str, Path], widget: Optional[QWidget] = None) -> Optional[QWidget]:
        """
        直接替代uic.loadUi
        """
        ui_path = Path(ui_path)
        with logger.contextualize(ui_path=str(ui_path)):
            if widget is None:
                widget = QWidget()
            if ui_path.suffix == ".py" and ui_path.exists():
                if UiLoader.load_py_ui(ui_path, widget):
                    return widget
                raise UiLoadError(ui_path, "无法加载 .py 文件")
            py_path = UiLoader.get_py_path_from_ui_path(ui_path)
            if py_path and py_path.exists():
                if UiLoader.load_py_ui(py_path, widget):
                    return widget
                logger.warning(f".py 文件存在但加载失败: {py_path}")
            # fallback 到 .ui 文件
            try:
                if not ui_path.is_absolute():
                    ui_path = CW_HOME / ui_path
                if ui_path.exists():
                    ui_file = QtCore.QFile(str(ui_path))
                    ui_file.open(QtCore.QFile.ReadOnly)  # type: ignore[attr-defined]
                    loader = QtUiTools.QUiLoader()
                    loaded_widget = loader.load(ui_file, widget)
                    ui_file.close()
                    # 将加载的.ui属性复制到传入的widget
                    if widget is not loaded_widget:
                        for attr_name in dir(loaded_widget):
                            if not attr_name.startswith('_'):
                                setattr(widget, attr_name, getattr(loaded_widget, attr_name))
                    widget.ui = loaded_widget  # type: ignore[attr-defined]
                    return widget
                raise FileNotFoundError(f"ui 文件不存在: {ui_path}")
            except Exception as e:
                raise UiLoadError(ui_path, str(e)) from e

    def load_multiple_ui(
        self,
        ui_paths: List[Union[str, Path]],
        widgets: Optional[List[QWidget]] = None,
        max_workers: int = 4,
    ) -> List[Optional[QWidget]]:
        """
        并行加载多个.ui文件
        """
        if widgets is None:
            widgets = [QWidget() for _ in ui_paths]
        if len(ui_paths) != len(widgets):
            raise ValueError("widget 数量不匹配")
        results: List[Optional[QWidget]] = [None] * len(ui_paths)
        py_paths = [
            (i, self.get_py_path_from_ui_path(p) or (Path(p) if Path(p).suffix == ".py" else None))
            for i, p in enumerate(ui_paths)
        ]
        valid_py_paths = [(i, p) for i, p in py_paths if p and p.exists()]
        modules = {}
        if valid_py_paths:
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                future_to_index = {
                    executor.submit(self._load_ui_module, py_path): i
                    for i, py_path in valid_py_paths
                }
                for future in as_completed(future_to_index):
                    i = future_to_index[future]
                    try:
                        modules[i] = future.result()
                    except Exception as e:
                        logger.error(f"预加载模块失败: {py_paths[i][1]} - {e}")
        for i, (ui_path, widget) in enumerate(zip(ui_paths, widgets)):
            ui_path_obj = Path(ui_path)
            with logger.contextualize(ui_path=str(ui_path_obj)):
                if modules.get(i):
                    try:
                        ui_class = next(
                            (
                                getattr(modules[i], attr)
                                for attr in dir(modules[i])
                                if isinstance((attr_val := getattr(modules[i], attr)), type)
                                and attr.startswith("Ui_")
                                and hasattr(attr_val, "setupUi")
                            ),
                            None,
                        )
                        if ui_class:
                            ui_instance = ui_class()
                            ui_instance.setupUi(widget)
                            if hasattr(ui_instance, "retranslateUi"):
                                ui_instance.retranslateUi(widget)
                            widget.ui = ui_instance  # type: ignore[attr-defined]
                            results[i] = widget
                            continue
                    except Exception as e:
                        logger.error(f"设置 .ui 失败: {ui_path} - {e}")
                # Fallback to single load_ui in main thread
                try:
                    results[i] = self.load_ui(ui_path, widget)
                except UiLoadError as e:
                    logger.error(str(e))
                    results[i] = None

        return results

    @staticmethod
    def load_ui_type(ui_path: Union[str, Path]) -> Tuple[type, type]:
        """
        这啥啊这是

        Return: (form_class, base_class)
        """
        ui_path = Path(ui_path)
        with logger.contextualize(ui_path=str(ui_path)):
            py_path = (
                ui_path if ui_path.suffix == '.py' else UiLoader.get_py_path_from_ui_path(ui_path)
            )
            if py_path and py_path.exists():
                module = UiLoader._load_ui_module(py_path)
                if module:
                    ui_class = next(
                        (
                            getattr(module, attr)
                            for attr in dir(module)
                            if isinstance((attr_val := getattr(module, attr)), type)
                            and attr.startswith("Ui_")
                            and hasattr(attr_val, "setupUi")
                        ),
                        None,
                    )
                    if ui_class:
                        base_class = ui_class.__bases__[0] if ui_class.__bases__ else QWidget
                        return ui_class, base_class
                logger.error(f"从 .py 文件加载 ui 类型失败: {py_path}")
            if ui_path.suffix == '.ui':
                if not ui_path.is_absolute():
                    ui_path = CW_HOME / ui_path
                try:
                    loader = QtUiTools.QUiLoader()
                    ui_file = QtCore.QFile(str(ui_path))
                    ui_file.open(QtCore.QFile.ReadOnly)  # type: ignore[attr-defined]
                    form_widget = loader.load(ui_file, None)
                    ui_file.close()
                    return form_widget.__class__, QWidget
                except Exception as e:
                    raise UiLoadError(ui_path, str(e)) from e
            raise UiLoadError(ui_path, "无法加载 ui 类型")


def load_ui(ui_path: Union[str, Path], widget: Optional[QWidget] = None) -> Optional[QWidget]:
    """
    直接替换uic.loadUi
    """
    return UiLoader.load_ui(ui_path, widget)


def load_ui_type(ui_path: Union[str, Path]) -> Tuple[type, type]:
    """
    直接替换uic.loadUiType
    """
    return UiLoader.load_ui_type(ui_path)


loadUiType = load_ui_type  # noqa: N816
loadUi = load_ui  # noqa: N816
