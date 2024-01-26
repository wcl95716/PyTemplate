import pyautogui
import uuid
import time
import threading
from typing import Callable
from pynput import keyboard

def click_back() -> None:
    x: float = 818.33203125
    y: float = 228.16015625
    pyautogui.click(x, y)

def screenshot() -> None:
    uuid_str: str = str(uuid.uuid4())
    png_path: str = f"data/test_paper/{uuid_str}.png"
    screenshot_image = pyautogui.screenshot()
    screenshot_image.save(png_path)

def run(stop_thread: threading.Event) -> None:
    while not stop_thread.is_set():
        screenshot()
        time.sleep(1.5)
        click_back()
        time.sleep(0.2)

def on_activate(stop_thread: threading.Event) -> None:
    if not stop_thread.is_set():
        print("Started")
        stop_thread.clear()
        threading.Thread(target=run, args=(stop_thread,)).start()
    else:
        print("Stopped")
        stop_thread.set()

def for_canonical(f: Callable[[keyboard.KeyCode], None]) -> Callable[[keyboard.KeyCode], None]:
    return lambda k: f(listener.canonical(k))

def on_activate_stop() -> None:
    print("Ending program")
    stop_thread.set()
    listener.stop()

stop_thread: threading.Event = threading.Event()

# 设置开始快捷键
start_hotkey: keyboard.HotKey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<shift>+r'),
    lambda: on_activate(stop_thread))

# 设置结束快捷键
stop_hotkey: keyboard.HotKey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<shift>+e'),
    on_activate_stop)

with keyboard.Listener(
        on_press=for_canonical(lambda k: start_hotkey.press(k) or stop_hotkey.press(k)),
        on_release=for_canonical(lambda k: start_hotkey.release(k) or stop_hotkey.release(k))) as listener:
    listener.join()
