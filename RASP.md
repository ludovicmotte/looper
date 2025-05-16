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
sudo apt-get update
sudo apt-get upgrade
sudo reboot

# if upgrade hangs:
# sudo apt-get remove real-vnc-server
```

# init bluetooth for bluetooth speaker

See https://pimylifeup.com/raspberry-pi-bluetooth/

```bash
sudo apt install -y bluetooth pi-bluetooth bluez blueman pavucontrol
```

## with GUI

Open Preferences / Bluetooth Manager
 - enable auto bluetooth
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
# find Audio / Sinks / JBL Flip 3 SE -> 80
wpctl set-default 80
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

wpctl status
# find Audio / Sources / BT600 Mono -> 91
wpctl set-default 91

arecord --format=S16_LE --duration=5 --rate=16000 --file-type=raw out.raw
aplay --format=S16_LE --rate=16000 out.raw
```

pulseaudio --start ??


# test button
```bash
watch -n 0.2 gpioget gpiochip0 2

python button.py
```
