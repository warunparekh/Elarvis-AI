import os

# Path to your Vosk model directory
VOSK_MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'vosk-model-small')

# Default music directory
MUSIC_DIR = r"C:\Users\<YourUser>\Music"

# Application launch mappings
APPS = {
    'notepad': r'C:\Windows\System32\notepad.exe',
    'calculator': r'C:\Windows\System32\calc.exe',
    'chrome': r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    # Add your own here
}

# OpenAI API key for chat mode (fallback to env variable)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")