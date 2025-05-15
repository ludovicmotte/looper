from gpiozero import Device, Button
from gpiozero.pins.rpigpio import RPiGPIOFactory

# Sélectionner explicitement RPiGPIO
Device.pin_factory = RPiGPIOFactory()

footswitch = Button(17, pull_up=True)
def on_press():
    print("Footswitch appuyé !")

footswitch.when_pressed = on_press
from signal import pause
pause()
