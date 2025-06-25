from sshkeyboard import listen_keyboard, stop_listening
from typing import Callable, Dict

# Dictionnaire des actions liées aux touches
keyboard_actions: Dict[str, Callable[[], None]] = {}


def press(key: str):
    if key in keyboard_actions:
        keyboard_actions[key]()
    # else:
    #    print(f"Touche non prise en charge : {key}")


def start_keyboard_listening(custom_actions: Dict[str, Callable[[], None]]):
    global keyboard_actions
    keyboard_actions = custom_actions
    listen_keyboard(on_press=press, until="")


def stop_keyboard_listening():
    stop_listening()


# Exemple d'utilisation
def main():
    start_keyboard_listening(
        {
            "1": lambda: print("1️"),
            "2": lambda: print("2️"),
            "3": lambda: print("3️"),
            "4": lambda: print("4️"),
            "5": lambda: print("5"),
            "q": stop_keyboard_listening,
        }
    )


if __name__ == "__main__":
    main()
