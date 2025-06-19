import os
import sys
import psutil

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QApplication
from loguru import logger
from PyQt5.QtCore import QSharedMemory, QTimer, QObject, pyqtSignal
import darkdetect
import datetime as dt

from file import base_directory, config_center
import signal

share = QSharedMemory('ClassWidgets')
_stop_in_progress = False

def restart():
    logger.debug('重启程序')
    app = QApplication.instance()
    if app:
        try:
            signal.signal(signal.SIGTERM, signal.SIG_DFL)
            signal.signal(signal.SIGINT, signal.SIG_DFL)
        except (AttributeError, ValueError):
            pass
        app.quit()
        app.processEvents()

    if share.isAttached():
        share.detach()  # 释放共享内存
    os.execl(sys.executable, sys.executable, *sys.argv)

def stop(status=0):
    global share, update_timer, _stop_in_progress
    if _stop_in_progress:
        return
    _stop_in_progress = True

    logger.debug('退出程序...')

    if 'update_timer' in globals() and update_timer:
        try:
            update_timer.stop()
            update_timer = None
        except Exception as e:
            logger.warning(f"停止全局更新定时器时出错: {e}")

    app = QApplication.instance()
    if app:
        try:
            signal.signal(signal.SIGTERM, signal.SIG_DFL)
            signal.signal(signal.SIGINT, signal.SIG_DFL)
        except (AttributeError, ValueError):
            pass
        app.quit()
    try:
        current_pid = os.getpid()
        parent = psutil.Process(current_pid)
        children = parent.children(recursive=True)
        if children:
            logger.debug(f"尝试终止 {len(children)} 个子进程...")
            for child in children:
                try:
                    logger.debug(f"终止子进程 {child.pid}...")
                    child.terminate()
                except psutil.NoSuchProcess:
                    logger.debug(f"子进程 {child.pid} 已不存在.")
                    continue
                except psutil.AccessDenied:
                    logger.warning(f"无权限终止子进程 {child.pid}.")
                    continue
                except Exception as e:
                    logger.warning(f"终止子进程 {child.pid} 时出错: {e}")

            gone, alive = psutil.wait_procs(children, timeout=1.5)
            if alive:
                logger.warning(f"{len(alive)} 个子进程未在规定时间内终止，将强制终止...")
                for p in alive:
                    try:
                        logger.debug(f"强制终止子进程 {p.pid}...")
                        p.kill()
                    except psutil.NoSuchProcess:
                        logger.debug(f"子进程 {p.pid} 在强制终止前已消失.")
                    except Exception as e:
                        logger.error(f"强制终止子进程 {p.pid} 失败: {e}")
    except psutil.NoSuchProcess:
        logger.warning("无法获取当前进程信息，跳过子进程终止。")
    except Exception as e:
        logger.error(f"终止子进程时出现意外错误: {e}")

    if 'share' in globals() and share:
        try:
            if share.isAttached():
                share.detach()
                logger.debug("共享内存已分离")
        except Exception as e:
            logger.error(f"分离共享内存时出错: {e}")

    logger.debug(f"程序退出({status})")
    if not app:
        os._exit(status)

def calculate_size(p_w=0.6, p_h=0.7):  # 计算尺寸
    screen_geometry = QApplication.primaryScreen().geometry()
    screen_width = screen_geometry.width()
    screen_height = screen_geometry.height()

    width = int(screen_width * p_w)
    height = int(screen_height * p_h)

    return (width, height), (int(screen_width / 2 - width / 2), 150)

def update_tray_tooltip():
    """更新托盘文字"""
    if hasattr(sys.modules[__name__], 'tray_icon'):
        tray_instance = getattr(sys.modules[__name__], 'tray_icon')
        if tray_instance is not None:
            schedule_name_from_conf = config_center.read_conf('General', 'schedule')
            if schedule_name_from_conf:
                try:
                    schedule_display_name = schedule_name_from_conf
                    if schedule_display_name.endswith('.json'):
                        schedule_display_name = schedule_display_name[:-5]
                    tray_instance.setToolTip(f'Class Widgets - "{schedule_display_name}"')
                    logger.info(f'托盘文字更新: "Class Widgets - {schedule_display_name}"')
                except Exception as e:
                    logger.error(f"更新托盘提示时发生错误: {e}")
            else:
                tray_instance.setToolTip("Class Widgets - 未加载课表")
                logger.info(f'托盘文字更新: "Class Widgets - 未加载课表"')

class DarkModeWatcher(QObject):
    darkModeChanged = pyqtSignal(bool)  # 发出暗黑模式变化信号
    def __init__(self, interval=500, parent=None):
        super().__init__(parent)
        self._isDarkMode = darkdetect.isDark()  # 初始状态
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._checkTheme)
        self._timer.start(interval)  # 轮询间隔（毫秒）

    def _checkTheme(self):
        currentMode = darkdetect.isDark()
        if currentMode != self._isDarkMode:
            self._isDarkMode = currentMode
            self.darkModeChanged.emit(currentMode)  # 发出变化信号

    def isDark(self):
        """返回当前是否暗黑模式"""
        return self._isDarkMode

    def stop(self):
        """停止监听"""
        self._timer.stop()

    def start(self, interval=None):
        """开始监听"""
        if interval:
            self._timer.setInterval(interval)
        self._timer.start()


class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon(f"{base_directory}/img/logo/favicon.png"))

    def push_update_notification(self, text=''):
        self.setIcon(QIcon(f"{base_directory}/img/logo/favicon-update.png"))  # tray
        self.showMessage(
            "发现 Class Widgets 新版本！",
            text,
            QIcon(f"{base_directory}/img/logo/favicon-update.png"),
            5000
        )

    def push_error_notification(self, title='检查更新失败！', text=''):
        self.setIcon(QIcon(f"{base_directory}/img/logo/favicon-update.png"))  # tray
        self.showMessage(
            title,
            text,
            QIcon(f"{base_directory}/img/logo/favicon-error.ico"),
            5000
        )


class UnionUpdateTimer(QObject):
    """
    统一更新计时器
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._on_timeout)
        self.callbacks = []  # 存储所有的回调函数
        self._is_running = False

    def _on_timeout(self):  # 超时
        app = QApplication.instance()
        if not app or app.closingDown():
            if self.timer.isActive():
                self.timer.stop()
            return

        # 使用最初的备份列表，防止遍历时修改
        callbacks_copy = self.callbacks[:]
        for callback in callbacks_copy:
            if callback in self.callbacks:
                try:
                    callback()
                except RuntimeError as e:
                    logger.error(f"回调调用错误 (可能对象已删除): {e}")
                    try:
                        self.callbacks.remove(callback)
                    except ValueError:
                        pass
                except Exception as e:
                    logger.error(f"执行回调时发生未知错误: {e}")
        if self._is_running:
            self._schedule_next()

    def _schedule_next(self):
        now = dt.datetime.now()
        next_tick = now.replace(microsecond=0) + dt.timedelta(seconds=1)
        delay = max(0, int((next_tick - now).total_seconds() * 1000))
        self.timer.start(delay)

    def add_callback(self, callback):
        if callback not in self.callbacks:
            self.callbacks.append(callback)
            if not self._is_running:
                self.start()

    def remove_callback(self, callback):
        try:
            self.callbacks.remove(callback)
        except ValueError:
            pass
        # if not self.callbacks and self._is_running:
        #     self.stop() # 删除定时器

    def remove_all_callbacks(self):
        self.callbacks = []
        # self.stop() # 删除定时器

    def start(self):
        if not self._is_running:
            logger.debug("启动 UnionUpdateTimer...")
            self._is_running = True
            self._schedule_next()

    def stop(self):
        self._is_running = False
        if self.timer:
            try:
                if self.timer.isActive():
                    self.timer.stop()
            except RuntimeError as e:
                logger.warning(f"停止 QTimer 时发生运行时错误: {e}")
            except Exception as e:
                logger.error(f"停止 QTimer 时发生未知错误: {e}")

def get_str_length(text: str) -> int:
    """
    计算字符串长度，汉字计为2，英文和数字计为1
    
    Args:
        text: 要计算的字符串
    
    Returns:
        int: 字符串长度
    """
    length = 0
    for char in text:
        # 使用 ord() 获取字符的 Unicode 码点
        # 如果大于 0x4e00 (中文范围开始) 就是汉字，计为2
        if ord(char) > 0x4e00:
            length += 2
        else:
            length += 1
    return length

def slice_str_by_length(text: str, max_length: int) -> str:
    """
    根据指定长度切割字符串，汉字计为2，英文和数字计为1
    
    Args:
        text: 要切割的字符串
        max_length: 最大长度
    
    Returns:
        str: 切割后的字符串
    """
    if not text or max_length <= 0:
        return ""
    
    if get_str_length(text) <= max_length:
        return text

    current_length = 0
    result = []

    for char in text:
        char_length = 2 if ord(char) > 0x4e00 else 1
        if current_length + char_length > max_length:
            break
        result.append(char)
        current_length += char_length

    return ''.join(result)

tray_icon = None
update_timer = UnionUpdateTimer()
