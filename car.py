"""
Carthing: python code to control an rc car using an rpi
    Copyright (C) 2017 Aaron Thomas

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
'''
probably want to just change init to setup all the pins to LOW and then change
the functions to set other pin to low and the correct one to HIGH
the cleanup setup hack worked temporarily and then we realized what the real problem is
iif yo fix the code as described in this comment it might perform a little faster
this is hackathon code btw
'''
import RPi.GPIO as GPIO

class CarController:
    def __init__(self):
        self.dirty = True
        self.forward_pin = 12
        self.backward_pin = 11
        self.left_pin = 16
        self.right_pin = 15
        GPIO.setmode(GPIO.BOARD)

    def accel_forward(self):
        if not self.dirty:
            return
        GPIO.cleanup(self.backward_pin)
        GPIO.setup(self.forward_pin, GPIO.OUT, initial=GPIO.HIGH)

    def accel_backward(self):
        if not self.dirty:
            return
        GPIO.cleanup(self.forward_pin)
        GPIO.setup(self.backward_pin, GPIO.OUT, initial=GPIO.HIGH)

    def accel_neutral(self):
        if not self.dirty:
            return
        GPIO.cleanup([self.forward_pin, self.backward_pin])

    def steer_left(self):
        if not self.dirty:
            return
        GPIO.cleanup(self.right_pin)
        GPIO.setup(self.left_pin, GPIO.OUT, initial=GPIO.HIGH)

    def steer_right(self):
        if not self.dirty:
            return
        GPIO.cleanup(self.left_pin)
        GPIO.setup(self.right_pin, GPIO.OUT, initial=GPIO.HIGH)

    def steer_neutral(self):
        if not self.dirty:
            return
        GPIO.cleanup([self.left_pin, self.right_pin])

    def cleanup(self):
        self.dirty=True
        GPIO.cleanup()
