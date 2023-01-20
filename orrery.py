#!/usr/bin/python3

from utils import to_seconds
from bodies import bodies


def orrery(days):
    print('After', days, 'Earth days, each celestial body will have orbited:')

    for body, value in bodies.items():
        new_theta = round(to_seconds(1, 'd') /
                          value['full_orbit']*360*days)
        print(body, '-', new_theta, 'deg')


orrery(90)
