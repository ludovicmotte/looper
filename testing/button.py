from gpiozero import Button
#             .___.              
#    +3V3---1-|O O|--2--+5V
#   GPIO2---3-|O O|--4--+5V
#   GPIO3---5-|O O|--6--_
#   GPIO4---7-|O O|--8-----GPIO14
#        _--9-|O.O|-10-----GPIO15
#  GPIO17--11-|O O|-12-----GPIO18
#  GPIO27--13-|O O|-14--_
#  GPIO22--15-|O O|-16-----GPIO23
#    +3V3--17-|O O|-18-----GPIO24
#  GPIO10--19-|O.O|-20--_
#  GPIO9 --21-|O O|-22-----GPIO25
#  GPIO11--23-|O O|-24-----GPIO8 
#        _-25-|O O|-26-----GPIO7 
#  ID_SD---27-|O O|-28-----ID_SC
#  GPIO5---29-|O.O|-30--_
#  GPIO6---31-|O O|-32-----GPIO12
#  GPIO13--33-|O O|-34--_
#  GPIO19--35-|O O|-36-----GPIO16
#  GPIO26--37-|O O|-38-----GPIO20
#        _-39-|O O|-40-----GPIO21
#             '---'
#  

# GPIO2 and 03 has a physical pull-up resistor
# Button default assumes the common pull-up circuit

# GPIO4 (pin 7)  and GRND (pin 6) + default pull_up
#button4 = Button(4)
#print("button4.value="+str(button4.value)+ " button4.pin.state="+str(button4.pin.state))
#button4.wait_for_press()
#print('You pushed me')
#print("button4.value="+str(button4.value)+ " button4.pin.state="+str(button4.pin.state))


# GPI14 (pin 8) and 3v3 (pin 1) + specific pull_up=False
button14 = Button(14, pull_up=False)
print("button14.value="+str(button14.value)+ " button14.pin.state="+str(button14.pin.state))
button14.wait_for_press()
print('You pushed me')
print("button14.value="+str(button14.value)+ " button14.pin.state="+str(button14.pin.state))
