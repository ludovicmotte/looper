# init project sources
```bash
mkdir workspace && cd workspace
git clone https://github.com/ludovicmotte/looper.git && cd looper
sudo apt install -y code
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

```bash
git config --global user.name "raspberry"
git config --global user.email "raspberry@pi.com"

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
watch -n 0.2 gpioget gpiochip0 17


sudo apt install python3-rpi.gpio

pip install gpiozero
python button.py
```



(myenv) axel@raspberrypi:~/workspace/looper $ python button.py 
/home/axel/workspace/looper/myenv/lib/python3.11/site-packages/gpiozero/devices.py:300: PinFactoryFallback: Falling back from lgpio: No module named 'lgpio'
  warnings.warn(
/home/axel/workspace/looper/myenv/lib/python3.11/site-packages/gpiozero/devices.py:300: PinFactoryFallback: Falling back from rpigpio: No module named 'RPi'
  warnings.warn(
/home/axel/workspace/looper/myenv/lib/python3.11/site-packages/gpiozero/devices.py:300: PinFactoryFallback: Falling back from pigpio: No module named 'pigpio'
  warnings.warn(
/home/axel/workspace/looper/myenv/lib/python3.11/site-packages/gpiozero/devices.py:297: NativePinFactoryFallback: Falling back to the experimental pin factory NativeFactory because no other pin factory could be loaded. For best results, install RPi.GPIO or pigpio. See https://gpiozero.readthedocs.io/en/stable/api_pins.html for more information.
  warnings.warn(NativePinFactoryFallback(native_fallback_message))
Traceback (most recent call last):
  File "/home/axel/workspace/looper/myenv/lib/python3.11/site-packages/gpiozero/pins/native.py", line 237, in export
    result = self._exports[pin]
             ~~~~~~~~~~~~~^^^^^
KeyError: 17

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/axel/workspace/looper/myenv/lib/python3.11/site-packages/gpiozero/pins/native.py", line 247, in export
    result = os.open(self.path_value(pin),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/sys/class/gpio/gpio17/value'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/axel/workspace/looper/button.py", line 5, in <module>
    footswitch = Button(17)
                 ^^^^^^^^^^
  File "/home/axel/workspace/looper/myenv/lib/python3.11/site-packages/gpiozero/devices.py", line 108, in __call__
    self = super().__call__(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/axel/workspace/looper/myenv/lib/python3.11/site-packages/gpiozero/input_devices.py", line 412, in __init__
    super().__init__(
  File "/home/axel/workspace/looper/myenv/lib/python3.11/site-packages/gpiozero/mixins.py", line 417, in __init__
    super().__init__(*args, **kwargs)
  File "/home/axel/workspace/looper/myenv/lib/python3.11/site-packages/gpiozero/input_devices.py", line 167, in __init__
    self.pin.edges = 'both'
    ^^^^^^^^^^^^^^
  File "/home/axel/workspace/looper/myenv/lib/python3.11/site-packages/gpiozero/pins/__init__.py", line 441, in <lambda>
    lambda self, value: self._set_edges(value),
                        ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/axel/workspace/looper/myenv/lib/python3.11/site-packages/gpiozero/pins/native.py", line 519, in _set_edges
    self.factory.fs.export(self._number)
  File "/home/axel/workspace/looper/myenv/lib/python3.11/site-packages/gpiozero/pins/native.py", line 251, in export
    with io.open(self.path('export'), 'wb') as f:
OSError: [Errno 22] Invalid argument