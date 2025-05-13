from gpiozero import Button

# GPIO2 and 03 has a physical pull-up resistor
# Button default assumes the common pull-up circuit

# pin 7 (GPIO4) and pin 6 (GRND) + default pull_up
button = Button(4)
print("button.value="+str(button.value)+ " button.pin.state="+str(button.pin.state))
button.wait_for_press()
print('You pushed me')
print("button.value="+str(button.value)+ " button.pin.state="+str(button.pin.state))


# pin 7 (GPIO4) and pin 1 (3v3) + specific pull_up=False
#button = Button(4, pull_up=False)
#print("button.value="+str(button.value)+ " button.pin.state="+str(button.pin.state))
#button.wait_for_press()
#print('You pushed me')
#print("button.value="+str(button.value)+ " button.pin.state="+str(button.pin.state))
