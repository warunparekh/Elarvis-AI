import queue
from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json
import pyttsx3
import assistant.config as config

engine = pyttsx3.init()
model = Model(path=config.VOSK_MODEL_PATH)
rec = KaldiRecognizer(model, 16000)
audio_queue = queue.Queue()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def callback(indata, frames, time, status):
    audio_queue.put(bytes(indata))


def start_listening():
    sd.InputStream(samplerate=16000, channels=1, callback=callback).start()


def listen():
    while True:
        data = audio_queue.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            return result.get('text', '')