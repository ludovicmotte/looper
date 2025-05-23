import sounddevice as sd
import numpy as np

def play_loop(audio_data: np.ndarray, sample_rate: int):

    duration_seconds = audio_data.shape[0] / sample_rate
    print(f"Sample rate: {sample_rate} Hz")
    print(f"Total duration of the loop: {duration_seconds:.2f} seconds")

    sd.stop() # Stop any previous playback
    # Infinite playback loop
    sd.play(audio_data, sample_rate, loop=True)


def stop_playing():
    sd.stop()

# Exemple d'utilisation
def main():
    mixed_audio = np.array([[0.5, 0.6, 0.7], [-0.5, -0.6, -0.7]])
    sample_rate = 44100
    play_loop(mixed_audio, sample_rate)


if __name__ == "__main__":
    main()
