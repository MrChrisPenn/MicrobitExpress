from microbit import *
import radio
radio.on()
while True:
  incoming -= radio.recieve()
  if incoming == "Forward":
    fwd()
  if incoming == "Back":
    rev()
  if incoming == "Stop":
    stp()

def fwd():
  pin8.write_digital(1)
  pin12.write_digital(0)
  pin0.write_digital(1)
  pin16.write_digital(0)

def stp():
  pin0.write_digital(0)
  pin0.write_digital(0)
  pin0.write_digital(0)
  pin0.write_digital(0)

def rev():
  pin8.write_digital(0)
  pin12.write_digital(1)
  pin0.write_digital(0)
  pin16.write_digital(1)
