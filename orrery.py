#!/usr/bin/python3

import utils
from bodies import bodies

print('After one Earth day, each celestial body will have orbited:')

for body, value in bodies.items():
    new_theta = utils.to_seconds(1, 'd')/value['full_orbit']*360
    print(body, new_theta)
