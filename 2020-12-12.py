#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:53:08 2020

@author: johan
"""


from aocd import get_data
import numpy as np

nav_data = get_data(day=12).split('\n')


test_data="""F10
N3
F7
R90
F11""".split('\n')



def first_challenge(data):
    debug = False
    direction = 0 # east = xpos>0 and ypos=0
    x,y = 0,0

    if debug : print(data)
    for line in data:
        dy = int(np.cos(np.deg2rad(direction)))
        dx = int(np.sin(np.deg2rad(direction)))
        instruction = line[0]
        amount = int(line[1:])
        if debug : print('EAST %2d, NORTH %2d and %3d degrees [%2d,%2d] ->  %s, %d' % (y,x, direction,dx,dy, instruction,amount), end ='')
        if instruction == 'F':
            x += amount*dx
            y += amount*dy
        elif instruction == 'N':
            x += amount
        elif instruction == 'S':
            x -= amount
        elif instruction == 'E':
            y += amount
        elif instruction == 'W':
            y -= amount
        elif instruction == 'R':
            direction -= amount
        elif instruction == 'L':
            direction += amount
        else:
            print('Error in line ', line)
        if debug : print('    -> new=  EAST %2d, NORTH %2d ' % (y,x))

    if debug : print('\n')
    return (abs(x)+abs(y))



def second_challenge(data):
    waypointx,waypointy = 1,10
    x,y = 0,0

    debug = False
    if debug : print(data)
    for line in data:
        instruction = line[0]
        amount = int(line[1:])
        if debug : print('EAST %2d, NORTH %2d, waypoint=[%d,%d]->  %s, %d' % (y,x, waypointx,waypointy, instruction,amount), end ='')
        if instruction == 'F':
            x += amount*waypointx
            y += amount*waypointy
        elif instruction == 'N':
            waypointx += amount
        elif instruction == 'S':
            waypointx -= amount
        elif instruction == 'E':
            waypointy += amount
        elif instruction == 'W':
            waypointy -= amount
        elif instruction == 'R':
            while amount > 0:
                t = waypointx
                waypointx = -waypointy
                waypointy = t
                amount -= 90
        elif instruction == 'L':
            while amount > 0:
                t = waypointx
                waypointx = waypointy
                waypointy = -t
                amount -= 90
        else:
            print('Error in line ', line)
        if debug : print('    -> new=  EAST %2d, NORTH %2d ' % (y,x))

    if debug : print('\n')
    return (abs(x)+abs(y))



print('First challenge testdata ' , first_challenge(test_data))
print('First challenge  realdata ' , first_challenge(nav_data))



print('Second challenge testdata ' , second_challenge(test_data))
print('Second challenge realdata ' , second_challenge(nav_data))


