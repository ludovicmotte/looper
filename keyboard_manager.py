from sshkeyboard import listen_keyboard, stop_listening
from typing import Callable, Dict

# Dictionnaire des actions liées aux touches
keyboard_actions: Dict[str, Callable[[], None]] = {}

def press(key: str):
    if key in keyboard_actions:
        keyboard_actions[key]()
    elif key in ['q', 'esc']:
        print("🛑 Arrêt de l'écoute clavier.")
        stop_listening()
    #else:
    #    print(f"Touche non prise en charge : {key}")

def start_keyboard_listening(custom_actions: Dict[str, Callable[[], None]]):
    global keyboard_actions
    keyboard_actions = custom_actions
    listen_keyboard(on_press=press)

# Exemple d'utilisation
def main():
    start_keyboard_listening({
        '1': lambda: print("1️⃣"),
        '2': lambda: print("2️⃣"),
        '3': lambda: print("3️⃣"),
        '4': lambda: print("4️⃣"),
        # Tu peux ajouter d'autres touches ici...
    })

if __name__ == "__main__":
    main()
