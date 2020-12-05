#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:37:01 2020

@author: johan
"""

from aocd import get_data
data = [int(x) for x in get_data(day=1).split('\n')]


print('Part 1')
for a in data:
    if 2020-int(a) in data:
        print(a*( 2020-a))

print('\nPart 2')
for a in data:
    for b in data:
        if 2020-a-b in data:
            print(a*b*(2020-a-b))


