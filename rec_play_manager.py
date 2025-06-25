import queue
import sys
import sounddevice as sd
import numpy as np

recording = False
q = queue.Queue()
samplerate = 44100
channels = 1
audio_data = []  # Liste pour accumuler les blocs audio


def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())


def on_pressed():
    global recording
    recording = not recording
    if recording:
        rec()
    else:
        play()


def rec():
    global audio_data
    print("let's rec")
    audio_data = []  # Réinitialiser les données
    with sd.InputStream(samplerate=samplerate, channels=channels, callback=callback):
        while recording:
            audio_data.append(q.get())


def play():
    global audio_data, recording
    if not audio_data:
        print("No data to play")
        return
    print("let's play in loop")
    # remet en ligne les blocs audio enregistrés par callback
    data = np.concatenate(audio_data, axis=0)
    while not recording:
        sd.play(data, samplerate)
        sd.wait()


def stop():
    global recording
    recording = True  # ce qui veut dire playing False
