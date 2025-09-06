"""
ui->py

view/**/*.ui -> view/py/**/*.py
ui/xxx/*.ui -> ui/xxx/py/*.py
ui/xxx/dark/*.ui -> ui/xxx/dark/py/*.py
"""

import concurrent.futures
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import List

from loguru import logger

sys.path.append(str(Path(__file__).resolve().parents[1]))
from basic_dirs import CW_HOME


class UIConverter:
    def __init__(self, max_workers=None):
        self.converted_files = []
        self.failed_files = []
        self.max_workers = max_workers or os.cpu_count()
        self.resource_files = []

    def fix_icon_paths(self, output_file: Path) -> bool:
        """修正图标路径并收集资源文件路径用于生成qrc文件"""
        try:
            content = output_file.read_text(encoding="utf-8")
            original_content = content

            # 定义资源文件模式
            resource_pattern = r'"([^"]+\.(?:svg|png|jpg|gif))"'

            # 先收集所有资源文件路径
            for match in re.finditer(resource_pattern, content):
                path = match.group(1).replace("\\", "/")

                # 根据路径类型确定实际文件位置
                if path.startswith(":/"):
                    # 已经是标准格式的路径
                    clean_path = path[2:]
                    res_path = CW_HOME / clean_path
                elif path.startswith(("subject/", "weather/")):
                    # 需要添加img前缀的路径
                    res_path = CW_HOME / "img" / path
                elif path.startswith(("audio/", "font/", "img/")):
                    # 直接添加到根目录的路径
                    res_path = CW_HOME / path
                elif "/" not in path:
                    # 裸文件名默认放img下
                    res_path = CW_HOME / "img" / path
                else:
                    # 其他路径尝试从项目根目录查找
                    res_path = CW_HOME / path

                # 检查文件是否存在并添加到资源列表
                if res_path.exists() and res_path not in self.resource_files:
                    logger.debug(f"找到资源文件: {res_path.relative_to(CW_HOME)}")
                    self.resource_files.append(res_path)

            # 然后修正路径
            def replacer(match: re.Match) -> str:
                path = match.group(1).replace("\\", "/")
                if path.startswith(":/"):
                    return f'"{path}"'
                if path.startswith("subject/"):
                    return f'":/img/{path}"'
                if path.startswith("weather/"):
                    return f'":/img/{path}"'
                if path.startswith("audio/"):
                    return f'":/{path}"'
                if path.startswith("font/"):
                    return f'":/{path}"'
                if path.startswith("img/"):
                    return f'":/{path}"'
                # 裸文件名默认放 img 下
                if "/" not in path:
                    return f'":/img/{path}"'
                return f'"{path}"'

            # 替换路径
            content = re.sub(resource_pattern, replacer, content)
            if content != original_content:
                with output_file.open("w", encoding="utf-8", newline="\n") as f:
                    f.write(content)
                logger.debug(f"已修正图标路径: {output_file.relative_to(CW_HOME)}")
            return True
        except Exception as e:
            logger.error(f"修正图标路径失败: {output_file.relative_to(CW_HOME)} - {e!s}")
            return False

    def convert_ui_to_py(self, ui_file: Path, output_file: Path) -> bool:
        try:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            cmd = [
                "pyside6-uic",
                str(ui_file),
                "-o",
                str(output_file),
            ]
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            self.fix_icon_paths(output_file)
            logger.success(
                f"转换成功: {ui_file.relative_to(CW_HOME)} -> {output_file.relative_to(CW_HOME)}"
            )
            self.converted_files.append((ui_file, output_file))
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"转换失败: {ui_file.relative_to(CW_HOME)} - {e.stderr}")
            self.failed_files.append((ui_file, str(e)))
            return False
        except Exception as e:
            logger.error(f"转换失败: {ui_file.relative_to(CW_HOME)} - {e!s}")
            self.failed_files.append((ui_file, str(e)))
            return False

    def find_ui_files(self, directory: Path) -> List[Path]:
        ui_files = []
        if directory.exists():
            for ui_file in directory.rglob("*.ui"):
                ui_files.append(ui_file)
        return ui_files

    def convert_view_files(self):
        """
        转换view的ui文件

        rule: view/**/*.ui -> view/py/**/*.py
        """
        view_dir = CW_HOME / "view"
        ui_files = self.find_ui_files(view_dir)
        conversion_tasks = []

        for ui_file in ui_files:
            rel_path = ui_file.relative_to(view_dir)
            output_path = view_dir / "py" / rel_path.with_suffix(".py")
            conversion_tasks.append((ui_file, output_path))
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [
                executor.submit(self.convert_ui_to_py, task[0], task[1])
                for task in conversion_tasks
            ]
            concurrent.futures.wait(futures)
        logger.success(f"已完成view文件转换, 共{len(ui_files)}个文件, 使用{self.max_workers}个线程")

    def convert_ui_theme_files(self):
        """
        转换主题的ui文件

        rule:
        - ui/xxx/*.ui -> ui/xxx/py/*.py
        - ui/xxx/dark/*.ui -> ui/xxx/dark/py/*.py
        """
        ui_dir = CW_HOME / "ui"
        if not ui_dir.exists():
            return

        conversion_tasks = []

        for theme_dir in ui_dir.iterdir():
            if not theme_dir.is_dir():
                continue
            theme_name = theme_dir.name
            logger.debug(f"处理主题: {theme_name}")
            # ui/xxx/目录下
            light_ui_files = list(theme_dir.glob("*.ui"))
            for ui_file in light_ui_files:
                output_path = theme_dir / "py" / ui_file.with_suffix(".py").name
                conversion_tasks.append((ui_file, output_path))
            # ui/xxx/dark目录下
            dark_dir = theme_dir / "dark"
            if dark_dir.exists():
                dark_ui_files = list(dark_dir.glob("*.ui"))
                for ui_file in dark_ui_files:
                    output_path = dark_dir / "py" / ui_file.with_suffix(".py").name
                    conversion_tasks.append((ui_file, output_path))

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [
                executor.submit(self.convert_ui_to_py, task[0], task[1])
                for task in conversion_tasks
            ]
            concurrent.futures.wait(futures)
        logger.success(
            f"已完成主题UI文件转换, 共{len(conversion_tasks)}个文件, 使用{self.max_workers}个线程"
        )

    def scan_resource_files(self):
        """
        扫描项目中的资源文件
        """
        # 扫描img目录下的所有图片资源
        img_dir = CW_HOME / "img"
        if img_dir.exists():
            for ext in ["*.svg", "*.png", "*.jpg", "*.gif"]:
                for file_path in img_dir.glob(f"**/{ext}"):
                    if file_path not in self.resource_files:
                        self.resource_files.append(file_path)

        # 扫描audio目录下的所有音频资源
        audio_dir = CW_HOME / "audio"
        if audio_dir.exists():
            for ext in ["*.wav", "*.mp3"]:
                for file_path in audio_dir.glob(f"**/{ext}"):
                    if file_path not in self.resource_files:
                        self.resource_files.append(file_path)

        # 扫描font目录下的所有字体资源
        font_dir = CW_HOME / "font"
        if font_dir.exists():
            for ext in ["*.ttf", "*.otf"]:
                for file_path in font_dir.glob(f"**/{ext}"):
                    if file_path not in self.resource_files:
                        self.resource_files.append(file_path)

        logger.info(f"扫描到{len(self.resource_files)}个资源文件")

    def generate_qrc_file(self):
        """
        生成.qrc文件
        """
        # 先扫描资源文件
        self.scan_resource_files()

        if not self.resource_files:
            logger.warning("没有发现资源文件")
            return

        resource_groups = {}
        for res_file in self.resource_files:
            file_ext = res_file.suffix.lower().lstrip('.')
            if file_ext not in resource_groups:
                resource_groups[file_ext] = []
            resource_groups[file_ext].append(res_file)

        qrc_path = CW_HOME / "resources.qrc"
        with open(qrc_path, "w", encoding="utf-8", newline="\n") as f:
            f.write('<!DOCTYPE RCC>\n<RCC version="1.0">\n')
            for res_type, files in resource_groups.items():
                f.write(f'  <qresource prefix="/{res_type}">\n')
                for res_file in files:
                    rel_path = res_file.relative_to(CW_HOME)
                    rel_path_str = str(rel_path).replace(os.sep, '/')
                    f.write(f'    <file>{rel_path_str}</file>\n')
                f.write('  </qresource>\n')
            f.write('</RCC>\n')

        logger.success(f"已生成qrc资源文件: {qrc_path}")
        py_rc_path = CW_HOME / "resources_rc.py"
        try:
            subprocess.run(["pyside6-rcc", str(qrc_path), "-o", str(py_rc_path)], check=True)
            logger.success(f"已生成Python资源文件: {py_rc_path}")
        except FileNotFoundError:
            logger.error("找不到 pyside6-rcc 编译器")
        except subprocess.CalledProcessError as e:
            logger.error(f"编译 qrc 文件失败: {e}")

    def generate_summary(self):
        if self.failed_files:
            logger.error("转换失败的文件:")
            for ui_file, error in self.failed_files:
                logger.error(f"- {ui_file.relative_to(CW_HOME)}: {error}")

    def run(self):
        logger.debug(f"根目录: {CW_HOME}")
        self.convert_view_files()
        self.convert_ui_theme_files()
        self.generate_qrc_file()
        self.generate_summary()
        return len(self.failed_files) == 0


def main():
    converter = UIConverter()
    success = converter.run()
    if success:
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
