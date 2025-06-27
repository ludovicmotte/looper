import threading
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
    
    # configure for each button the when_pressed thread
    button_t_plus.when_pressed = lambda: threading.Thread(target=t_plus_action).start()
    button_t_minus.when_pressed = lambda: threading.Thread(target=t_minus_action).start()
    button_rec_play.when_pressed = lambda: threading.Thread(target=mute_unmute_action).start()
    button_mute_unmute.when_pressed = lambda: threading.Thread(target=mute_unmute_action).start()
    button_save.when_pressed = lambda: threading.Thread(target=save_action).start()



# Exemple d'utilisation
def main():

    def simulate_pressed(message, delay = 1):
        print(message)
        time.sleep(delay)

    start_buttons_listening(
        lambda: simulate_pressed("button_t_plus pressed"),
        lambda: simulate_pressed("button_t_minus pressed"),
        lambda: simulate_pressed("button_rec_play pressed", 10),
        lambda: simulate_pressed("button_mute_unmute pressed"),
        lambda: simulate_pressed("button_save pressed")
    )
    time.sleep(60)


if __name__ == "__main__":
    main()
