import time
from gpiozero import Button
from typing import Callable


# GPIO21 pin 40 and GRND pin 39 + default pull_up
button_t_plus = Button(21, bounce_time=0.1)

# GPIO5 pin 29 and GRND pin 30 + default pull_up
button_t_minus = Button(5, bounce_time=0.1)

# GPIO23 pin 16 and GRND pin 14 + default pull_up
button_rec_play = Button(23, bounce_time=0.1)

# GPIO14 pin 8 and GRND pin 6 + default pull_up
button_mute_unmute = Button(14, bounce_time=0.1)

# GPIO4 pin 7 and GRND pin 9 + default pull_up
button_save = Button(4, bounce_time=0.1)


def start_buttons_listening(
        t_plus_action: Callable[[], None],
        t_minus_action: Callable[[], None],
        rec_play_action: Callable[[], None],
        mute_unmute_action: Callable[[], None],
        save_action: Callable[[], None]):
    
    button_t_plus.when_pressed = t_plus_action
    button_t_minus.when_pressed = t_minus_action
    button_rec_play.when_pressed = rec_play_action
    button_mute_unmute.when_pressed = mute_unmute_action
    button_save.when_pressed = save_action



# Exemple d'utilisation
def main():

    def on_rec_play_pressed():
        print("rec/play pressed")
        time.sleep(5)

    start_buttons_listening(
        lambda: print ("button_t_plus pressed"),
        lambda: print ("button_t_minus pressed"),
        on_rec_play_pressed,
        lambda: print ("button_mute_unmute pressed"),
        lambda: print ("button_save pressed")
    )
    time.sleep(60)


if __name__ == "__main__":
    main()
