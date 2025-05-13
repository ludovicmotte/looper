# install latest OS
With Raspberry Pi Imager, install latest Raspberry Pi OS into the SD card.

# on first boot
Create a user  
Update OS  
Restart

# init project sources
```bash
mkdir workspace && cd workspace
git clone https://github.com/ludovicmotte/looper.git && cd looper
sudo apt install -y code
git config --global user.name "raspberry"
git config --global user.email "raspberry@pi.com"
```

Open Programming / Visual Studio Code, then directory ~/workspace/looper

# init system
```bash
#if not done during first boot
sudo apt-get update
sudo apt-get upgrade
# if upgrade hangs:
# sudo apt-get remove real-vnc-server
sudo reboot
```

# init bluetooth for bluetooth speaker

See https://pimylifeup.com/raspberry-pi-bluetooth/

```bash
# not usefull
# sudo apt install -y bluetooth pi-bluetooth bluez blueman pavucontrol
```

## with GUI

Open  Bluetooth Manager
 - search
 - pair
 - trust
 - connect

Output sound to JBL Flip 3 SE

Test with
```bash
aplay bass.wav
```


## with CLI
```bash
export DEVICE="5C:FB:7C:77:F1:11"

bluetoothctl
agent on
scan on
pair $DEVICE
trust $DEVICE
connect $DEVICE
quit
```

Output sound to JBL Flip 3 SE
```bash
wpctl status
# find Audio / Sinks / JBL Flip 3 SE -> 75
wpctl set-default 75
```


Test with
```bash
aplay bass.wav
```


# init USB mic
See https://iotbytes.wordpress.com/connect-configure-and-test-usb-microphone-and-speaker-with-raspberry-pi/

```bash
aplay -l
arecord -l

# give card 3 device 0

wpctl status
# find Audio / Sources / BT600 Mono -> 85
wpctl set-default 91

arecord --format=S16_LE --duration=5 --rate=16000 --file-type=raw out.raw
aplay --format=S16_LE --rate=16000 out.raw
```


# test button
```bash
watch -n 0.2 gpioget gpiochip0 2
```

With venv:
```bash
pip install gpiozero
pip install RPi.lGPIO
```
or
```bash
python3 -m venv --system-site-packages myenv
```

```bash
python button.py
```

sudo apt install -y python3.11-venv
python3 -m venv --system-site-packages myenv
source myenv/bin/activate
pip install pynput
python keyboard_manager.py

Listening for keys 1–4 and ‘q’ to quit. Press ‘q’ to stop.
1️ is pressed
12️ is pressed
2

