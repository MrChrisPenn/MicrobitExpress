#remote
from microbit import *
import radio


radio.on()
speed = 0
while True:
    

    if button_a.was_pressed():
        speed = speed + 1
        radio.send(str(speed))
        display.scroll(str(speed))
        
    
    if button_b.was_pressed():
        radio.send('Stop')
        display.scroll('S')