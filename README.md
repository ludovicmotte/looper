# Python setup

```bash
sudo apt update
sudo apt install -y python3.12-venv
python3 -m venv myenv
source myenv/bin/activate
```


# dependencies installation
```bash
sudo apt install -y libportaudio2 portaudio19-dev pulseaudio
pip install sounddevice scipy sshkeyboard soundfile
```

Ton code Python
        ↓
sounddevice (Python)
        ↓
    PortAudio (C)
        ↓
[vers PulseAudio ou ALSA]
        ↓
[Son joué dans Windows via WSLg]



# run
```bash
export PULSE_SERVER=unix:/mnt/wslg/PulseServer
python rec_play.py
```


# debug

```bash
sudo apt install alsa-utils
aplay bass.wav

#import sounddevice as sd
#print(sd.query_devices())
```

