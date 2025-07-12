import os, subprocess, psutil
import pyautogui, random
from assistant.config import APPS, MUSIC_DIR
from assistant.utils import list_music_files


def open_app(name):
    path = APPS.get(name.lower())
    if path and os.path.exists(path):
        subprocess.Popen(path)
        return f"Opened {name}."
    return f"App '{name}' not found."


def close_app(name):
    for proc in psutil.process_iter(['name']):
        if name.lower() in proc.info['name'].lower():
            proc.kill()
            return f"Closed {name}."
    return f"No running process for '{name}'."


def play_music(filename=None):
    files = list_music_files(MUSIC_DIR)
    target = filename if filename in files else random.choice(files)
    subprocess.Popen(['vlc', '--intf', 'dummy', os.path.join(MUSIC_DIR, target)])
    return f"Playing {target}."


def select_all_and_delete():
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    return "Deleted all selected files."