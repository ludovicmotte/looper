from gpiozero import Button
from signal import pause


footswitch = Button(17, pull_up=True)

def on_press():
    print("Footwwitch appuyé !")

footswitch.when_pressed = on_press


pause()