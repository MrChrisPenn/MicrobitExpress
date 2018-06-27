from microbit import *
import radio
radio.on()
def fwd():
  pin8.write_digital(0)
  pin12.write_digital(1)
  display.scroll("R")
  sleep(1000)
def rev():
  pin8.write_digital(1)
  pin12.write_digital(0)
  display.scroll("R")
def stp():
  pin8.write_digital(0)
  pin12.write_digital(0)
  display.scroll("S")
while True:
  incoming=radio.receive()
  if incoming == "Forward":
    fwd()
  if incoming == "Back":
    rev()
  if incoming == "Stop":
    stp()
  if incoming == "WST":
    fwd()
