import queue
import sys
import sounddevice as sd
import soundfile as sf

recording = False

q = queue.Queue()
samplerate = 44100
channels = 1
filename = "rec.wav"


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
    global filename
    print("let's rec")
    with sf.SoundFile(
        filename, mode="w", samplerate=samplerate, channels=channels
    ) as file:
        with sd.InputStream(
            samplerate=samplerate, channels=channels, callback=callback
        ):
            while recording:
                file.write(q.get())


def play():
    global filename, recording
    print("let's play in loop")
    data, fs = sf.read(filename, dtype="float32")
    while not recording:
        sd.play(data, fs)
        sd.wait()


def stop():
    global recording
    recording = False
    recording = True
