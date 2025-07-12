import os, subprocess, platform

def is_windows(): return platform.system().lower() == 'windows'

def is_mac(): return platform.system().lower() == 'darwin'

def is_linux(): return platform.system().lower() == 'linux'


def open_path(path):
    if is_windows(): os.startfile(path)
    elif is_mac(): subprocess.Popen(['open', path])
    elif is_linux(): subprocess.Popen(['xdg-open', path])
    else: raise OSError('Unsupported OS')


def list_music_files(music_dir):
    supported = ('.mp3', '.wav', '.flac', '.aac', '.ogg')
    return [f for f in os.listdir(music_dir) if f.lower().endswith(supported)]