#!/usr/bin/env python3
import numpy as np
import sounddevice as sd


def play_tone(frequency, duration, samplerate=44100):
    """
    Joue un son pur (sinusoïde) de fréquence (Hz) pendant duration (s).
    """
    t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
    wave = 0.2 * np.sin(2 * np.pi * frequency * t)  # amplitude réduite (0.2)
    sd.play(wave, samplerate)
    sd.wait()


def play_melody():
    # Exemple : do (261), ré (293), mi (329), do (261)
    notes = [
        (261.63, 0.2),
        (293.66, 0.2),
        (329.63, 0.2),
        (261.63, 0.4),
        (293.66, 0.2),
        (329.63, 0.2),
        (261.63, 0.4),
    ]
    for freq, dur in notes:
        play_tone(freq, dur)


if __name__ == "__main__":
    # --- votre code principal ici ---
    # ...
    # À la fin, on joue la mélodie :
    play_melody()
