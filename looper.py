from buttons_managers import start_buttons_listening
from keyboard_manager_WSL import start_keyboard_listening, stop_keyboard_listening
from rec_play_manager import on_pressed, stop
from start import play_melody
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
    print("rec/play pressed")
    on_pressed()


def on_save_pressed():
    print("save pressed...but currently not implemented")


def on_quit_pressed():
    print("❌")
    stop_keyboard_listening()
    stop()


# Main program
def main():

    # joue la mélodie qui permet de savoir que le script a bien été lancé
    play_melody()

    # Démarrer l'écoute boutons
    start_buttons_listening(
        on_t_plus_pressed,
        on_t_minus_pressed,
        on_rec_play_pressed,
        on_toggle_mute,
        on_save_pressed,
    )

    # Démarrer l'écoute du clavier
    start_keyboard_listening(
        {
            "+": on_t_plus_pressed,
            "-": on_t_minus_pressed,
            "r": on_rec_play_pressed,
            "m": on_toggle_mute,
            "s": on_save_pressed,
            "q": on_quit_pressed,
            "esc": on_quit_pressed,
        }
    )


if __name__ == "__main__":
    main()
