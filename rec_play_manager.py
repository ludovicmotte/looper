import queue
import sys
import time
import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import read

recording = False

q = queue.Queue()
samplerate = 44100
channels = 1
filename="rec.wav"


def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

def on_pressed():
    global recording
    recording = not recording
    if (recording):
        rec()
    else:
        play()

def rec():
    global filename
    print("let's rec")
    with sf.SoundFile(filename, mode='w', samplerate=samplerate,
                    channels=channels) as file:
        with sd.InputStream(samplerate=samplerate,
                            channels=channels, callback=callback):
            while recording:
                file.write(q.get())
    
def play():
    global filename
    print("let's play")
    data = read(filename)
    sd.play(data, samplerate)
    sd.wait()