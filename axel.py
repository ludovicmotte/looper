from keyboard_manager_WSL import start_keyboard_listening, stop_keyboard_listening

recording = False

def on_1_pressed():
    global recording
    if (recording):
        print("let's play")
    else:
        print("let's rec")
    recording = not recording

def on_quit_pressed():
    print("❌")
    stop_keyboard_listening()

# Main program
def main():

    # Démarrer l'écoute du clavier
    start_keyboard_listening(
        {
            "1": on_1_pressed,
            "esc": on_quit_pressed,
        }
    )


if __name__ == "__main__":
    main()