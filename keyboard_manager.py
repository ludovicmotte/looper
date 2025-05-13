from pynput import keyboard
from typing import Callable, Dict

# Dictionary mapping key.char (or key.name) to actions
keyboard_actions: Dict[str, Callable[[], None]] = {}

# The listener object (so we can stop it later)
_listener: keyboard.Listener | None = None


def on_press(key: keyboard.Key | keyboard.KeyCode):
    try:
        k = key.char  # single-char keys
    except AttributeError:
        k = key.name  # special keys

    if k in keyboard_actions:
        keyboard_actions[k]()


def start_keyboard_listening(custom_actions: Dict[str, Callable[[], None]]):
    """
    Replace the global actions dict and start listening.
    """
    global keyboard_actions, _listener
    keyboard_actions = custom_actions

    # Create and start a listener in a non-blocking thread
    _listener = keyboard.Listener(on_press=on_press)
    _listener.start()


def stop_keyboard_listening():
    """
    Stops the listener thread cleanly.
    """
    global _listener
    if _listener:
        _listener.stop()
        _listener = None


def main():
    start_keyboard_listening(
        {
            "1": lambda: print("1️ is pressed"),
            "2": lambda: print("2️ is pressed"),
            "3": lambda: print("3️ is pressed"),
            "4": lambda: print("4️ is pressed"),
            "q": stop_keyboard_listening,
        }
    )

    print("Listening for keys 1–4 and ‘q’ to quit. Press ‘q’ to stop.")
    # Keep the main thread alive while listener is running
    try:
        while _listener and _listener.is_alive():
            _listener.join(timeout=0.1)
    except KeyboardInterrupt:
        stop_keyboard_listening()


if __name__ == "__main__":
    main()
