#remote
from microbit import *
import radio


radio.on()
speed = 0

while True:
    
    if button_a.was_pressed():
        radio.send('Forward')
        speed = speed+1
        display.scroll(str(speed))
        if speed == 10:
            speed  = 0
        
    
    if button_b.was_pressed():
        radio.send('Stop')
        display.scroll('S')