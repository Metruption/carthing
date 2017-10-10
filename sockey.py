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
the url should be some json file with a dictionary {'x':something,'y':something}
where x and y both coorespond to an int value between -1 and 1
x is steering -1 left and 1 is right
y is acceleration 1 forward -1 backward
0 means neutral for both
this is hackathon code btw
'''
import json
import requests

import car
c = car.CarController()

def event_to_driving(shit):
    if shit['x'] == -1:
        c.steer_left()
    elif shit['x'] == 0:
        c.steer_neutral()
    elif shit['x'] == 1:
        c.steer_right()
    if shit['y'] == -1:
        c.accel_backward()
    elif shit['y'] == 0:
        c.accel_neutral()
    elif shit['y'] == 1:
        c.accel_forward()


url = 'example.com/example.json'
while True:
    print(json.loads(requests.get(url).text))
