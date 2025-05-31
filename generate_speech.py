import asyncio
import hashlib
import os
import platform
import re
import time
from pathlib import Path
from typing import Optional
from contextlib import contextmanager

import edge_tts
import pyttsx3
from pyttsx3.voice import Voice
import pythoncom
from loguru import logger
from file import config_center

# 默认用常量
DEFAULT_SPEED = 50
MAX_PYTTSX3_RATE = 400
MIN_PYTTSX3_RATE = 50
DEFAULT_TIMEOUT = 10.0
DEFAULT_RETRIES = 5
DEFAULT_RETRY_DELAY = 1.0
MIN_VALID_FILE_SIZE = 10
CACHE_MAX_AGE = 86400  # 缓存最大保存时间(秒)


async def _get_edge_voices_async():
    """获取Edge TTS语音列表"""
    try:
        edge_voices = await edge_tts.list_voices()
        return [
            {"name": voice["FriendlyName"], "id": f"edge:{voice['Name']}"}
            for voice in edge_voices
            if _is_zh_voice(voice["Locale"])
        ]
    except Exception as e:
        logger.error(f"获取 Edge TTS 语音列表失败: {e}")
        return []


async def _get_pyttsx3_voices_async():
    """获取Pyttsx3语音列表"""
    try:
        with _pyttsx3_context() as engine:
            if not engine:
                return []
            voices_available = await asyncio.to_thread(engine.getProperty, "voices")
            return [
                {"name": voice.name, "id": f"pyttsx3:{voice.id}"}
                for voice in voices_available
                if _is_zh_pyttsx3_voice(voice)
            ]
    except OSError as oe:
        if oe.winerror == -2147221005:
            logger.warning(
                "系统语音引擎(pyttsx3/SAPI5)初始化失败，可能是组件未正确注册或损坏。将跳过加载系统语音。"
            )
        elif platform.system() != "Windows":
            logger.warning(
                f"在 {platform.system()} 上获取 Pyttsx3 语音列表时发生OS错误: {oe}。" "这可能是因为系统未安装或配置兼容的TTS引擎。将跳过加载系统语音。"
            )
        else:
            logger.error(f"获取 Pyttsx3 语音列表时发生OS错误: {oe}")
        return []
    except Exception as e:
        logger.error(f"获取 Pyttsx3 语音列表失败: {e}")
        return []


def _is_zh_voice(locale: str) -> bool:
    """检查是否为中文语音"""
    return "zh" in locale.lower()


def _is_zh_pyttsx3_voice(voice: Voice) -> bool:
    """检查pyttsx3中文语音"""
    name = voice.name.lower()
    if hasattr(voice, "languages") and voice.languages:
        return any("zh" in lang.lower() for lang in voice.languages)
    if "chinese" in name or "mandarin" in name:
        return True
    return False


@contextmanager
def _pyttsx3_context():
    """安全的pyttsx3引擎上下文管理器"""
    engine = None
    try:
        pythoncom.CoInitialize()
        engine = pyttsx3.init()
        yield engine
    except Exception as e:
        logger.error(f"pyttsx3引擎初始化失败: {e}")
        yield None
    finally:
        if engine:
            try:
                engine.stop()
            except Exception:
                pass
        try:
            pythoncom.CoUninitialize()
        except Exception:
            pass


def filter_zh_voices(voices: list) -> list:
    """筛选中文语音"""
    return [v for v in voices if "zh" in v.get("id", "").lower()]


def log_voices_summary(voices: list):
    """记录语音统计信息"""
    edge_count = len([v for v in voices if v["id"].startswith("edge:")])
    pyttsx3_count = len([v for v in voices if v["id"].startswith("pyttsx3:")])

    if edge_count > 0:
        logger.info(f"筛选了 {edge_count} 个 Edge 语音")
    if pyttsx3_count > 0:
        logger.info(f"筛选了 {pyttsx3_count} 个 Pyttsx3 语音")
    if not voices:
        logger.warning("未能获取到任何 TTS 语音")

_tts_voices_cache = {
    "edge": {"voices": [], "timestamp": 0},
    "pyttsx3": {"voices": [], "timestamp": 0},
}

async def get_tts_voices(engine_filter: Optional[str] = None):
    """异步获取可用的TTS语音列表(中文)，包括Edge和Pyttsx3.
    Args:
        engine_filter (Optional[str], optional): 指定引擎 ("edge" or "pyttsx3"). Defaults to None (获取所有).
    Returns:
        list: 语音列表,每个元素是 {'name': '显示名称', 'id': '引擎:语音ID'}
    """
    current_time = time.time()
    if engine_filter and engine_filter in _tts_voices_cache:
        cache_entry = _tts_voices_cache[engine_filter]
        if cache_entry["voices"] and (
            current_time - cache_entry["timestamp"] < CACHE_MAX_AGE
        ):
            return cache_entry["voices"]
    elif not engine_filter:
        all_cached = True
        combined_voices = []
        for eng, cache_entry in _tts_voices_cache.items():
            if not cache_entry["voices"] or (
                current_time - cache_entry["timestamp"] >= CACHE_MAX_AGE
            ):
                all_cached = False
                break
            combined_voices.extend(cache_entry["voices"])
        if all_cached:
            return combined_voices
    voices = []
    if engine_filter is None or engine_filter == ENGINE_EDGE:
        edge_voices = await _get_edge_voices_async()
        if edge_voices:
            voices.extend(edge_voices)
            _tts_voices_cache[ENGINE_EDGE]["voices"] = edge_voices
            _tts_voices_cache[ENGINE_EDGE]["timestamp"] = current_time
        else:
            logger.warning("Edge语音获取失败，不缓存其结果。")
    if engine_filter is None or engine_filter == ENGINE_PYTTSX3:
        pyttsx3_voices = await _get_pyttsx3_voices_async()
        if pyttsx3_voices:
            voices.extend(pyttsx3_voices)
            _tts_voices_cache[ENGINE_PYTTSX3]["voices"] = pyttsx3_voices
            _tts_voices_cache[ENGINE_PYTTSX3]["timestamp"] = current_time
        else:
            logger.warning("pyttsx3语音获取失败，不缓存其结果。")

    await asyncio.to_thread(log_voices_summary, voices)

    return voices


def get_voice_id_by_name(name: str, engine_filter: Optional[str] = None):
    """
    根据语音名称查找语音ID
    参数：
        name (str): 语音显示名称
        engine_filter (Optional[str]): 可选的引擎过滤器
    返回：
        str 或 None: 语音ID，如果未找到则返回None
    """
    voices = get_tts_voices(engine_filter)
    for v in voices:
        if v["name"] == name:
            return v["id"]
    return None


def get_voice_name_by_id(
    voice_id: str, available_voices: Optional[list] = None
) -> Optional[str]:
    """
    根据语音ID查找语音名称
    参数：
        voice_id (str): 语音ID
        available_voices (list, optional): 预先获取的语音列表,默认None(重新获取)
    返回：
        str 或 None: 语音名称,如果未找到则返回None
    """
    voices = available_voices if available_voices is not None else get_tts_voices()
    return next((v["name"] for v in voices if v["id"] == voice_id), None)


# 一些多复用常量
ENGINE_EDGE = "edge"
ENGINE_PYTTSX3 = "pyttsx3"
LANG_ZH = "zh-CN"
LANG_EN = "en-US"
CACHE_DIR_NAME = "cache"
AUDIO_DIR_NAME = "audio"
DEFAULT_TTS_TIMEOUT = 10.0
DEFAULT_DELETE_RETRIES = 5
DEFAULT_DELETE_DELAY = 1.0

class TTSEngine:
    """支持多平台和智能语音选择的多引擎TTS工具类"""

    def __init__(self):
        """
        初始化TTS引擎实例
        属性：
        - cache_dir: 音频缓存目录路径（软件运行目录下 cache/audio文件夹）
        - engine_priority: 引擎优先级列表
        - voice_mapping: 跨平台语音映射配置表
        """
        self.cache_dir = os.path.join(os.getcwd(), CACHE_DIR_NAME, AUDIO_DIR_NAME)
        self._ensure_cache_dir()
        self.engine_priority = [ENGINE_EDGE, ENGINE_PYTTSX3]
        self.voice_mapping = {
            ENGINE_EDGE: {LANG_ZH: "zh-CN-YunxiNeural", LANG_EN: "en-US-AriaNeural"},
            ENGINE_PYTTSX3: self._get_platform_voices(),
        }

    @staticmethod
    def _get_platform_voices():
        """
        获取当前平台的默认语音配置

        返回：
        - dict: 包含中英文语音ID的字典，结构为{'zh-CN': voice_id, 'en-US': voice_id}

        平台支持：
        - Windows: 使用注册表路径标识语音
        - macOS: 使用Apple语音标识符
        - Linux: 使用espeak语音名称
        """
        current_os = platform.system()
        platform_voices = {
            "Windows": {
                LANG_ZH: "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ZH-CN_HUIHUI_11.0",
                # LANG_EN: 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0'
            },
            "Darwin": {  # macOS
                LANG_ZH: "com.apple.speech.synthesis.voice.ting-ting.premium",
                # LANG_EN: 'com.apple.speech.synthesis.voice.Alex'
            },
            "Linux": {
                LANG_ZH: "zh-CN",
                # LANG_EN: 'en-US'
            },
        }
        return platform_voices.get(current_os, platform_voices["Linux"])

    def _ensure_cache_dir(self):
        Path(self.cache_dir).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _generate_filename(text: str, engine: str) -> str:
        timestamp = str(int(time.time()))
        hash_str = hashlib.md5(text.encode()).hexdigest()[:8]
        return f"{engine}_{hash_str}_{timestamp}.mp3"

    @staticmethod
    async def _edge_tts(text: str, voice: str, file_path: str) -> str:
        # 语速范围 0-100
        speed_value = int(config_center.read_conf("TTS", "speed"))
        rate_percentage = (speed_value - 50) * 2
        rate_str = f"{rate_percentage:+}%"
        logger.debug(f"Edge TTS Rate: {rate_str} (Slider: {speed_value})")
        communicate = edge_tts.Communicate(text, voice, rate=rate_str)
        await communicate.save(file_path)
        return file_path

    async def _pyttsx3_tts(self, text: str, voice: str, file_path: str) -> str:
        asyncio.get_running_loop()
        return await asyncio.to_thread(self._sync_pyttsx3, text, voice, file_path)

    @contextmanager
    def _pyttsx3_context(self):
        """pyttsx3引擎的上下文管理器，确保资源正确释放"""
        engine = None
        try:
            pythoncom.CoInitialize()
            engine = pyttsx3.init()
            yield engine
        except OSError as oe:
            if hasattr(oe, "winerror") and oe.winerror == -2147221005:
                logger.error(
                    "系统语音引擎(pyttsx3/SAPI5)初始化失败，无法使用此引擎生成语音。请检查系统语音组件。"
                )
                raise RuntimeError("pyttsx3/SAPI5 初始化失败") from oe
            else:
                logger.error(f"pyttsx3 初始化时发生OS错误: {oe}")
                raise RuntimeError("pyttsx3 初始化OS错误") from oe
        except Exception as init_e:
            logger.error(f"pyttsx3 初始化失败: {init_e}")
            raise RuntimeError("pyttsx3 初始化异常") from init_e
        finally:
            pythoncom.CoUninitialize()
            if engine:
                try:
                    engine.stop()
                except Exception as e:
                    logger.warning(f"关闭pyttsx3引擎时出错: {e}")

    @staticmethod
    def _sync_pyttsx3(text: str, voice: str, file_path: str):
        """同步生成语音文件（pyttsx3引擎）"""
        with TTSEngine()._pyttsx3_context() as engine:
            engine.connect("started-utterance", lambda name: None)
            engine.connect("finished-utterance", lambda name, completed: engine.stop())

            if voice:
                voices = engine.getProperty("voices")
                found_voice = next((v for v in voices if v.id == voice), None)
                if not found_voice:
                    voice_id_only = voice.split(":", 1)[-1]
                    found_voice = next(
                        (v for v in voices if v.id == voice_id_only), None
                    )
                if found_voice:
                    engine.setProperty("voice", found_voice.id)
                else:
                    logger.warning(
                        f"pyttsx3: 无效或不匹配的语音ID '{voice}'，将使用默认语音"
                    )
            speed_value = int(config_center.read_conf("TTS", "speed"))
            default_rate = engine.getProperty("rate")
            if speed_value == 50:
                pyttsx3_rate = default_rate
            elif speed_value < 50:
                # 0-50范围映射到0.5-1.0倍速
                pyttsx3_rate = int(
                    default_rate / 2 + (default_rate / 2) * (speed_value / 50)
                )
            else:
                # 50-100范围映射到1.0-1.5倍速
                pyttsx3_rate = int(
                    default_rate + (default_rate * 0.5) * ((speed_value - 50) / 50)
                )
            MIN_RATE = 50
            MAX_RATE = 400
            pyttsx3_rate = max(MIN_RATE, min(pyttsx3_rate, MAX_RATE))
            logger.debug(
                f"pyttsx3 Rate: {pyttsx3_rate} (Slider: {speed_value}, Default: {default_rate})"
            )
            engine.setProperty("rate", pyttsx3_rate)
            engine.save_to_file(text, file_path)
            start_time = time.time()
            engine.startLoop(False)
            PYTTSX3_TIMEOUT = DEFAULT_TTS_TIMEOUT
            ITERATION_SLEEP = 0.1
            while engine.isBusy():
                if time.time() - start_time > PYTTSX3_TIMEOUT:
                    logger.warning(
                        f"pyttsx3生成超时（{PYTTSX3_TIMEOUT}秒），尝试强制停止引擎。"
                    )
                    engine.stop()
                    raise TimeoutError(f"pyttsx3生成超时（{PYTTSX3_TIMEOUT}秒）")
                time.sleep(ITERATION_SLEEP)
                engine.iterate()

            engine.endLoop()

            return file_path

    @staticmethod
    def _detect_language(text: str) -> str:
        """检测文本语言（中文或英文）

        参数:
            text: 要检测的文本

        返回:
            语言代码: 'zh-CN' 或 'en-US'
        """
        if re.search("[一-鿿]", text):
            return LANG_ZH
        return LANG_EN

    def _validate_pyttsx3_voice(self, voice_id: str, lang: str) -> str:
        """验证pyttsx3语音ID有效性，并在无效时自动回退

        参数:
            voice_id: 要验证的语音ID
            lang: 语言代码

        返回:
            有效的语音ID或空字符串（表示无法使用pyttsx3）
        """
        try:
            with self._pyttsx3_context() as engine:
                voices = engine.getProperty("voices")
                if any(v.id == voice_id for v in voices):
                    return voice_id
                lang_voices = [v for v in voices if lang in str(v.languages)]
                if lang_voices:
                    logger.info(f"找到{lang}语言的替代语音: {lang_voices[0].id}")
                    return lang_voices[0].id

                default_voice = engine.getProperty("voice")
                if default_voice:
                    logger.info(f"使用默认语音: {default_voice}")
                    return default_voice
                else:
                    logger.warning("pyttsx3无可用默认语音，无法回退。")
                    return ""

        except (OSError, RuntimeError) as e:
            logger.warning(f"pyttsx3语音验证过程中发生引擎错误，无法使用pyttsx3: {e}")
            return ""
        except Exception as e:
            logger.error(f"pyttsx3语音验证失败: {str(e)}")
            return ""

    async def _execute_engine(
        self, engine: str, text: str, voice: str, file_path: str, timeout: float
    ) -> str:
        """
        生成语音文件的核心异步方法

        参数：
        text (str): 要转换的文本内容（支持中英文自动检测）
        engine (str): 首选TTS引擎（默认edge）
        voice (str): 指定语音ID（可选），不指定则根据语言自动选择
        auto_fallback (bool): 引擎失败时是否自动回退（默认False）
        timeout (float): 单引擎超时时间（秒，默认10）
        filename (str): 自定义文件名（可选），不指定则自动生成

        返回：
        str: 生成的音频文件绝对路径

        异常：
        ValueError: 如果提供的语音ID与指定的引擎不匹配
        RuntimeError: 所有尝试的引擎均失败时抛出
        """
        if voice and not voice.startswith(f"{engine}:"):
            raise ValueError(f"语音ID '{voice}' 与引擎 '{engine}' 不匹配")

        actual_voice_id = voice.split(":", 1)[1] if voice and ":" in voice else voice
        try:
            if engine == "edge":
                task = self._edge_tts(text, actual_voice_id, file_path)
            elif engine == "pyttsx3":
                task = self._pyttsx3_tts(text, actual_voice_id, file_path)
            else:
                raise ValueError(f"不支持的引擎：{engine}")

            return await asyncio.wait_for(task, timeout=timeout)
        except asyncio.TimeoutError:
            raise RuntimeError(f"{engine}引擎执行超时")
        except Exception as e:
            raise RuntimeError(f"{engine}引擎错误：{str(e)}")

    def _select_voice_for_engine(
        self, engine: str, lang: str, voice: Optional[str] = None
    ) -> str:
        """为指定引擎和语言选择合适的语音

        参数:
            engine: 引擎名称
            lang: 语言代码
            voice: 可选的指定语音ID

        返回:
            选择的语音ID
        """
        if voice:
            return voice
        if engine not in self.voice_mapping:
            logger.warning(f"未知引擎: {engine}，无法选择语音")
            return ""

        selected_voice = self.voice_mapping[engine].get(lang, "")
        if engine == ENGINE_PYTTSX3 and selected_voice:
            return self._validate_pyttsx3_voice(selected_voice, lang)

        return selected_voice

    async def generate_speech(
        self,
        text: str,
        engine: str = ENGINE_EDGE,
        voice: Optional[str] = None,
        auto_fallback: bool = False,
        timeout: float = DEFAULT_TTS_TIMEOUT,
        filename: Optional[str] = None,
    ) -> str:
        """生成语音文件的核心方法

        参数：
            text: 要转换的文本内容
            engine: 首选TTS引擎（默认edge）
            voice: 指定语音ID（可选）
            auto_fallback: 引擎失败时是否自动回退
            timeout: 单引擎超时时间（秒）
            filename: 自定义文件名（可选）

        返回：
            生成的音频文件绝对路径

        异常：
            RuntimeError: 所有尝试的引擎均失败时抛出
        """
        lang = self._detect_language(text)
        voice = self._select_voice_for_engine(engine, lang, voice)
        _filename = filename or self._generate_filename(text, engine)
        _file_path = os.path.join(self.cache_dir, _filename)
        if os.path.exists(_file_path):
            logger.info(f"语音文件已存在于缓存中，直接返回: {_file_path}")
            return _file_path
        engines_to_try = []
        if engine:
            engines_to_try.append(engine)
        if auto_fallback:
            for e in self.engine_priority:
                if e not in engines_to_try:
                    engines_to_try.append(e)
        if not engines_to_try and self.engine_priority:
            engines_to_try.append(self.engine_priority[0])

        if not engines_to_try:
            raise RuntimeError("没有可用的TTS引擎配置。")
        errors = []
        attempted_engines = set()
        for current_engine in engines_to_try:
            if current_engine in attempted_engines:
                continue
            attempted_engines.add(current_engine)
            if voice and ":" in voice and not voice.startswith(current_engine + ":"):
                logger.debug(f"跳过引擎 '{current_engine}'，语音ID不匹配")
                continue
            current_filename = (
                filename if filename else self._generate_filename(text, current_engine)
            )
            current_file_path = os.path.join(self.cache_dir, current_filename)

            if os.path.exists(current_file_path):
                logger.info(
                    f"目标语音文件 '{current_filename}' 在执行前已存在，直接返回"
                )
                return current_file_path

            try:
                await self._execute_engine(
                    engine=current_engine,
                    text=text,
                    voice=voice,
                    file_path=current_file_path,
                    timeout=timeout,
                )
                if not os.path.exists(current_file_path):
                    raise RuntimeError(f"语音文件生成后未找到: {current_file_path}")
                file_size = os.path.getsize(current_file_path)
                if file_size < 10:  # 小于10kb应该是损坏的
                    raise RuntimeError(f"生成的文件可能已损坏（大小: {file_size}字节）")

                logger.success(
                    f"成功生成语音 | 引擎: {current_engine} | 文件: {current_filename}"
                )
                return current_file_path
            except ValueError as ve:
                # 一般都是是语音ID不匹配
                logger.debug(f"跳过引擎 '{current_engine}': {ve}")
            except Exception as e:
                error_msg = f"{current_engine}: {str(e)}"
                errors.append(error_msg)
                logger.error(f"引擎 {current_engine} 生成失败: {e}")
                if os.path.exists(current_file_path):
                    try:
                        os.remove(current_file_path)
                        logger.debug(f"清理错误生成的文件: {current_file_path}")
                    except OSError as rm_err:
                        logger.warning(f"清理失败文件时出错: {rm_err}")
                if not auto_fallback:
                    logger.info(f"引擎 '{current_engine}' 失败后停止尝试")
                    break
                continue
        raise RuntimeError(f"所有引擎尝试失败\n" + "\n".join(errors))

    def cleanup(self, max_age: int = 86400):
        """清理过期缓存文件"""
        now = time.time()
        for f in Path(self.cache_dir).glob("*.*"):
            if f.is_file() and (now - f.stat().st_mtime) > max_age:
                logger.info(f"清理过期文件: {f.name}")
                self.delete_audio_file(str(f))

    @staticmethod
    def delete_audio_file(
        file_path: str,
        retries: int = DEFAULT_DELETE_RETRIES,
        delay: float = DEFAULT_DELETE_DELAY,
    ):
        """
        安全删除音频文件，包含多次重试和强制删除机制

        参数:
            file_path: 要删除的文件路径
            retries: 重试次数
            delay: 重试间隔(秒)

        返回:
            bool: 删除是否成功
        """
        if not file_path:
            logger.warning("尝试删除空文件路径")
            return False
        try:
            relative_path = os.path.relpath(
                file_path, os.path.join(os.getcwd(), CACHE_DIR_NAME, AUDIO_DIR_NAME)
            )
        except ValueError:
            relative_path = file_path
        if not os.path.exists(file_path):
            logger.debug(f"删除时文件已不存在: {relative_path}")
            return True
        try:
            with open(file_path, "rb") as _:
                pass
        except Exception as e:
            logger.warning(
                f"文件无法访问，可能已损坏或被锁定: {relative_path} | 错误: {e}"
            )
        for attempt in range(retries):
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
                    logger.debug(
                        f"成功删除文件: {relative_path} (尝试 {attempt+1}/{retries})"
                    )
                return True
            except PermissionError:
                logger.warning(
                    f"删除文件权限不足，等待后重试: {relative_path} (尝试 {attempt+1}/{retries})"
                )
                time.sleep(delay * (attempt + 1))
            except OSError as e:
                logger.warning(
                    f"删除文件时出现OS错误: {e} (尝试 {attempt+1}/{retries})"
                )
                time.sleep(delay * (attempt + 1))
        try:
            logger.warning(f"常规删除失败，尝试强制删除: {relative_path}")

            if platform.system() == "Windows":
                import subprocess

                subprocess.run(
                    [
                        "powershell",
                        "-Command",
                        f"Remove-Item -Path '{file_path}' -Force",
                    ],
                    capture_output=True,
                    text=True,
                    check=False,
                )
            else:  # Linux/Mac
                os.system(f"rm -f '{file_path}'")
            if not os.path.exists(file_path):
                logger.info(f"强制删除成功: {relative_path}")
                return True
        except Exception as e:
            logger.error(f"强制删除失败: {e}")
        try:
            file_size = (
                os.path.getsize(file_path) if os.path.exists(file_path) else "未知"
            )
            file_mtime = (
                time.ctime(os.path.getmtime(file_path))
                if os.path.exists(file_path)
                else "未知"
            )
            logger.error(
                f"无法删除文件: {relative_path} | 大小: {file_size} | 修改时间: {file_mtime}"
            )
        except Exception as e:
            logger.error(f"获取文件信息失败: {e}")

        return False


def generate_speech_sync(
    text: str,
    engine: str = "edge",
    voice: Optional[str] = None,
    auto_fallback: bool = False,
    timeout: float = 10.0,
    filename: Optional[str] = None,
) -> str:
    """同步生成方法"""
    tts = TTSEngine()
    return asyncio.run(
        tts.generate_speech(
            text=text,
            engine=engine,
            voice=voice,
            auto_fallback=auto_fallback,
            timeout=timeout,
            filename=filename,
        )
    )


def list_pyttsx3_voices():
    """列出所有可用的 Pyttsx3 语音."""
    try:
        try:
            engine = pyttsx3.init()
        except OSError as oe:
            if oe.winerror == -2147221005:
                logger.warning(
                    "系统语音引擎(pyttsx3/SAPI5)初始化失败，无法列出系统语音。"
                )
                return []
            else:
                logger.error(f"列出语音时 pyttsx3 初始化发生OS错误: {oe}")
                return []
        except Exception as init_e:
            logger.error(f"列出语音时 pyttsx3 初始化失败: {init_e}")
            return []

        voices = engine.getProperty("voices")
        engine.stop()
        voice_list = []
        for voice in voices:
            voice_list.append({"name": voice.name, "id": voice.id})
        return voice_list
    except Exception as e:
        logger.error(f"列出 Pyttsx3 语音时出错: {e}")
        return []
