#!/usr/bin/python3

from utils import to_seconds
from bodies import bodies

day=(int)(input("Enter no of days"))

def orrery(days):
    print('After', days, 'Earth days, each celestial body will have orbited:')

    for body, value in bodies.items():
        value['theta'] = round(to_seconds(1, 'd') /
                               value['full_orbit']*360*days)
        print(body, '-', value['theta'], 'deg')


orrery(day)
