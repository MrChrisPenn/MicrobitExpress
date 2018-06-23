"""
    run_motors.py

    This micro:bit MicroPython script uses k_motor.py to run 2 motors connected to
    the kitronik motor driver board.

    https://www.kitronik.co.uk/5620-motor-driver-board-for-the-bbc-microbit-v2.html

    The MIT License (MIT)

    Copyright (c) 2018 Alan Yorinks

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""
# start of k_motor.py
from microbit import pin0, pin8, pin12, pin16, display, Image

class KMotor:
    """
    This class is used to control 2 motors with the Kitronic
    Motor Driver Board
    """
    
    # Motor Directions
    FORWARD = 0
    REVERSE = 1

    # Motor Selectors
    MOTOR_1 = 0
    MOTOR_2 = 1

    def __init__(self):
        """
        Turn of both motors and clear the display
        """
        self.motor_off(KMotor.MOTOR_1)
        self.motor_off(KMotor.MOTOR_2)
        display.clear()

    def motor_on(self, motor, direction, speed=100):
        """
        Turn motor with the given direction and speed
        :param motor: KMotor.MOTOR1 or KMotor.Motor2
        :param direction: KMotor.FORWARD or KMOTOR.REVERSE
        :param speed: 0 - 100
        :return:
        """
        # make sure the speed is within range
        if not 0 <= speed <= 100:
            # not display a "NO" and return
            display.show(Image.NO)
            return

        # speed needs to be scaled from 0-100 to 0-1023
        speed = self._scale(speed)

        # Move Motor Forward
        if direction == KMotor.FORWARD:
            if motor == KMotor.MOTOR_1:
                pin8.write_analog(speed)
                pin12.write_digital(0)
            elif motor == KMotor.MOTOR_2:
                pin0.write_analog(speed)
                pin16.write_digital(0)

        # Move Motor In Reverse
        else:
            if motor == KMotor.MOTOR_1:
                pin12.write_analog(speed)
                pin8.write_digital(0)
            elif motor == KMotor.MOTOR_2:
                pin16.write_analog(speed)
                pin0.write_digital(0)

    def motor_off(self, motor):
        """
        Place motor in coast mode
        :param motor: KMotor.MOTOR1 or KMotor.Motor2
        :return:
        """
        if motor == KMotor.MOTOR_1:
            pin8.write_analog(0)
            pin12.write_analog(0)
        else:
            pin0.write_analog(0)
            pin16.write_analog(0)

    def motor_brake(self, motor):
        """
        Brake the selected motor.
        :param motor:
        :return:
        """
        if motor == KMotor.MOTOR_1:
            pin8.write_digital(1)
            pin12.write_digital(1)
        else:
            pin0.write_digital(1)
            pin16.write_digital(1)

    def _scale(self, value):
        """
        Scale the speed from 0-100 to 0-1023
        :param value: 0-100
        :return: scaled speed
        """
        new_value = (1023 / 100) * value
        return int(new_value)

# end of k_motory.py

# start of application

# application imports
from microbit import sleep
from microbit import *
import radio
from microbit import display, Image, button_a,button_b, sleep
# create an instance of KMotor
r = KMotor()

radio.on()
while True:
    if button_a.was_pressed():
        radio.send('Forward')  #Forward message
    elif button_a.is_pressed() and button_b.is_pressed():
        radio.send("Stop")
    elif button_b.was_pressed():
        radio.send('Back')  #Back
        
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == 'Forward':
        # turn motor 1 on in forward for 1 second and turn it off
        
        #r.motor_on(r.MOTOR_2, r.FORWARD)
        display.scroll('F')
        #sleep(3000)
        r.motor_on(r.MOTOR_1, r.FORWARD,100)
        #sleep(5000)
        #r.motor_off(r.MOTOR_1)
        #sleep(2000)
        #r.motor_on(r.MOTOR_1, r.REVERSE,100)
    if incoming == 'Stop':
        
        #r.motor_off(r.MOTOR_2)
        display.scroll('S')
        r.motor_off(r.MOTOR_1)

    if incoming == 'Back':
        
        #r.motor_off(r.MOTOR_2)
        display.scroll('B')
        r.motor_on(r.MOTOR_1, r.REVERSE,100)

    
    
