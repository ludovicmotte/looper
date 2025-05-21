from player import play_in_loop, stop_playing
from keyboard_manager import start_keyboard_listening, stop_keyboard_listening


def on_1_pressed():
    print("1️⃣")
    play_in_loop(["testing/beat.wav"])

def on_2_pressed():
    print("2️⃣")
    play_in_loop(["testing/beat.wav", "testing/synth.wav"])

def on_3_pressed():
    print("3️⃣")
    play_in_loop(["testing/beat.wav", "testing/synth.wav", "testing/voice.wav"])

def on_4_pressed():
    print("4️⃣")
    play_in_loop(["testing/beat.wav", "testing/synth.wav", "testing/pluck.wav"])

def on_quit_pressed():
    print("❌")
    stop_playing()
    stop_keyboard_listening()


# Main program
def main():

    # Démarrer l'écoute du clavier
    start_keyboard_listening({
        '1': on_1_pressed,
        '2': on_2_pressed,
        '3': on_3_pressed,
        '4': on_4_pressed,
        'q': on_quit_pressed,
        'esc': on_quit_pressed,
    })



if __name__ == "__main__":
    main()
