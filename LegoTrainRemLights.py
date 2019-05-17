from microbit import *
import radio
radio.on()
def lights_on():
    pin0.write_digital(1)

def lights_off():
        pin0.write_digital(0)

def fwd():
    pin8.write_digital(1)
    pin12.write_digital(0)
def stp():
    pin8.write_digital(0)
    pin12.write_digital(0)
def rev():
    pin8.write_digital(0)
    pin12.write_digital(1)
while True:
    incoming = radio.receive()
    if incoming == 'fwd':
        fwd()
        lights_on()
    if incoming == 'stp':
        stp()
        lights_off()
    if button_a.was_pressed():
        radio.send('fwd') 
        #fwd()
        #lights_on()
    if button_b.was_pressed():
        radio.send('stp') 
        #stp()
        #lights_off()
