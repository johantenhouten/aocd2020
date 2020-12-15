#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:21:24 2020

@author: johan
"""

from aocd import get_data

timetable = get_data(day=13).split('\n')

testdata="""939
7,13,x,x,59,x,31,19""".split('\n')

def first_challenge(data):

    arrival = int(data[0])
    busses = [ int(x) for x in data[1].split(',') if x != 'x']
    bestbus = 0
    besttime = max(busses)


    for bus in busses:
        last_bus = arrival // bus
        if (last_bus+1) * bus - arrival < besttime:
            bestbus = bus
            besttime = (last_bus+1) * bus - arrival

    return (bestbus * besttime)


def second_challenge(data):
    busses = data[1].split(",")
    arrivaltimes = {}
    for index,bus in enumerate(busses):
        if bus != 'x':
            arrivaltimes[int(bus)] = (int(bus)-index) % int(bus)

    busses = [int(bus) for bus in busses if bus != 'x']
    arrivaltime = arrivaltimes[busses[0]]

    step = busses[0]
    for bus in busses[1:]:
        while arrivaltime % bus != arrivaltimes[bus]:
            arrivaltime += step
        step *= bus
    return arrivaltime


print('First challenge testdata', first_challenge( testdata)  )
print('First challenge real data', first_challenge( timetable)  )

print('Second challenge testdata', second_challenge( testdata)  )
print('Second challenge testdata', second_challenge( """1\n7,13,x,x,59,x,31,19""".split('\n')   ))
print('Second challenge other testdata', second_challenge( """1\n17,x,13,19""".split('\n')   ))
print('Second challenge other testdata', second_challenge( """1\n67,7,59,61""".split('\n')   ))
print('Second challenge other testdata', second_challenge( """1\n67,x,7,59,61""".split('\n')   ))
print('Second challenge other testdata', second_challenge( """1\n67,7,x,59,61""".split('\n')   ))
print('Second challenge other testdata', second_challenge( """1\n1789,37,47,1889""".split('\n')   ))
print('Second challenge real data', second_challenge(timetable   ))















