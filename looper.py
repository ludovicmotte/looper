from keyboard_manager_WSL import start_keyboard_listening, stop_keyboard_listening
from rec_play_manager import on_pressed, stop
from tracks_manager import tracks_manager


def on_t_plus_pressed():
    print("t+ pressed")
    tracks_manager.t_plus()


def on_t_minus_pressed():
    print("t- pressed")
    tracks_manager.t_minus()


def on_toggle_mute():
    print("mute/unmute pressed")
    tracks_manager.toggle_mute()


def on_rec_play_pressed():
    print("rec/paly pressed")
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
            "+": on_t_plus_pressed,
            "-": on_t_minus_pressed,
            "m": on_toggle_mute,
            "r": on_rec_play_pressed,
            "q": on_quit_pressed,
            "esc": on_quit_pressed,
        }
    )


if __name__ == "__main__":
    main()
