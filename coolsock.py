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
this was trying to use sse to talk to the server and I diidn't feel like making
it work so this file is useless. including it because someone might find it useful
'''
import json
import time
from sseclient import SSEClient

# import car
#
# c = car.CarController()
#
# def event_to_driving(shit):
#     if shit['x'] == -1:
#         c.steer_left()
#     elif shit['x'] == 0:
#         c.steer_neutral()
#     elif shit['x'] == 1:a
#         c.steer_right()
#     if shit['y'] == -1:
#         c.accel_backward()
#     elif shit['y'] == 0:
#         c.accel_neutral()
#     elif shit['y'] == 1:
#         c.accel_forward()


messages = SSEClient('https://rc-proje.firebaseio.com/move.json',retry=(100))
for msg in messages:
    print(json.loads(msg.data,"timestamp",int(round(time.time() * 1000)))
    # event_to_driving(json.loads(msg))
