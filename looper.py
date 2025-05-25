from audio_manager import read_audio_file
from audio_player import stop_playing
from keyboard_manager_WSL import start_keyboard_listening, stop_keyboard_listening
from tracks_manager import TrackManager


track_manager = TrackManager()
file_paths = [
    "testing/beat.wav",
    "testing/synth.wav",
    "testing/pluck.wav",
    "testing/voice.wav",
]
for i, file_path in enumerate(file_paths, start=1):
    audio_data, sample_rate = read_audio_file(file_path)
    track_manager.set_track(i, audio_data, sample_rate, False)


def on_1_pressed():
    print("1️⃣")
    track_manager.toggle_track(1)


def on_2_pressed():
    print("2️⃣")
    track_manager.toggle_track(2)


def on_3_pressed():
    print("3️⃣")
    track_manager.toggle_track(3)


def on_4_pressed():
    print("4️⃣")
    track_manager.toggle_track(4)


def on_quit_pressed():
    print("❌")
    stop_playing()
    stop_keyboard_listening()


# Main program
def main():

    # Démarrer l'écoute du clavier
    start_keyboard_listening(
        {
            "1": on_1_pressed,
            "2": on_2_pressed,
            "3": on_3_pressed,
            "4": on_4_pressed,
            "q": on_quit_pressed,
            "esc": on_quit_pressed,
        }
    )


if __name__ == "__main__":
    main()
