from microbit import *
import radio
radio.on()

option = 0

while True:
    
    sleep(250)
    option = option + button_a.get_presses()
    display.scroll(str(option))
    if button_a.is_pressed() and button_b.is_pressed():
        option = 0
    elif button_b.was_pressed():
        if option == 0: #stop
            display.scroll("S")
            radio.send("Stop")
        elif option == 1:#fwd
            display.scroll("F")
            radio.send("Forward")
        elif option == 2:#bck
            display.scroll("R")
            radio.send("Back")
        elif option == 3:#Worlds smallest track
            display.scroll("WST")
            radio.send("WST")
        