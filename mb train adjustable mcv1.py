from microbit import *
import radio

def stop():
    pin8.write_analog(1023)
    pin12.write_analog(1023)

def forward(speed):
    pin8.write_analog(speed)
    pin12.write_digital(0)
    display.scroll(speed)

    
speed = 0

radio.on()
while True:
    incoming = radio.receive()
    if incoming == 'Forward':
        msg = 'FW GO'+str(speed)
        display.scroll(msg)
        speed = speed +100
        if speed == 1000:
            speed = 0
        #Cycles = 0
        #while Cycles < 4:
        forward(speed)
        
    if button_b.was_pressed() or incoming == 'Stop':
        display.scroll('FW stop')
        stop()