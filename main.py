from assistant.voice import speak, listen, start_listening
from assistant.commands import open_app, close_app, play_music, select_all_and_delete
from assistant.chat import chat


def parse_and_execute(command):
    cmd = command.lower()
    if 'open' in cmd:
        return open_app(cmd.replace('open', '').strip())
    if 'close' in cmd:
        return close_app(cmd.replace('close', '').strip())
    if 'play music' in cmd:
        return play_music()
    if 'delete all' in cmd or 'select all and delete' in cmd:
        return select_all_and_delete()
    # Fallback to conversational chat mode
    return chat(command)


if __name__ == '__main__':
    print("Starting Elarvis AI...")
    start_listening()
    while True:
        speak("How can I help?")
        text = listen()
        if not text:
            continue
        print(f"You said: {text}")
        response = parse_and_execute(text)
        print(f"Assistant: {response}")
        speak(response)