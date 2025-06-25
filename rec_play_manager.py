import queue
import sys
import sounddevice as sd


q = queue.Queue()
samplerate = 44100
channels = 2


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())


def rec():
    with sd.InputStream(samplerate=samplerate,
                        channels=channels, callback=callback):
        print('rec')
  
def play():
    print('play')