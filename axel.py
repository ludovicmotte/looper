from keyboard_manager_WSL import start_keyboard_listening, stop_keyboard_listening
from rec_play_manager import on_pressed, stop


def on_1_pressed():
    on_pressed()


def on_quit_pressed():
    print("❌")
    stop_keyboard_listening()
    stop()


# Main program
def main():

    # Démarrer l'écoute du clavier
    start_keyboard_listening(
        {
            "1": on_1_pressed,
            "q": on_quit_pressed,
            "esc": on_quit_pressed,
        }
    )


if __name__ == "__main__":
    main()
