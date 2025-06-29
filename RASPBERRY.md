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

# Python setup

```bash
sudo apt update
sudo apt install -y python3.12-venv
python3 -m venv --system-site-packages myenv
source myenv/bin/activate
```

# test button
```bash
watch -n 0.2 gpioget -B pull-up gpiochip0 4
watch -n 0.2 gpioget -B pull-down gpiochip0 14
python testing/button.py
```

~~With simple venv:~~
```bash
# pip install gpiozero
# pip install RPi.lGPIO
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
wpctl set-default 73

arecord --format=S16_LE --duration=5 --rate=16000 --file-type=raw out.raw
aplay --format=S16_LE --rate=16000 out.raw
```

# start python script at statup

sudo vi /etc/systemd/system/looper.service
```
[Unit]
Description=Lance mon script looper.py au démarrage
After=multi-user.target

[Service]
Type=simple
User=axel
WorkingDirectory=/home/axel/workspace/looper
ExecStart=/home/axel/workspace/looper/myenv/bin/python /home/axel/workspace/looper/looper.py
Restart=on-failure
```


Rechargez systemd et activez le service
```bash
sudo systemctl daemon-reload
sudo systemctl enable looper.service
```

Testez immédiatement sans redémarrer :
```bash
sudo systemctl start looper.service
sudo journalctl -u looper.service -f
```


# TODO

```bash
pip install pynput
python keyboard_manager.py
```


Crée un service utilisateur :

mkdir -p ~/.config/systemd/user
nano ~/.config/systemd/user/looper.service


[Unit]
Description=Script qui demarre looper.py
After=default.target

[Service]
Type=simple
ExecStart=/home/axel/workspace/looper/myenv/bin/python /home/axel/workspace/looper/looper.py
WorkingDirectory=/home/axel/workspace/looper
Restart=on-failure
Environment=DISPLAY=:0
Environment=XDG_RUNTIME_DIR=/run/user/1000

[Install]
WantedBy=default.target



Activer le service utilisateur :

systemctl --user daemon-reload
systemctl --user enable myscript.service
systemctl --user start myscript.service



Et pour qu’il se lance automatiquement au boot :

loginctl enable-linger pi