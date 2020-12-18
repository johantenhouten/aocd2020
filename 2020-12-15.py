#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:51:10 2020

@author: johan
"""

from aocd import get_data

data =get_data(day=15).split(',')


testdata = ['a','b','c']
realdata = [12,20,0,6,1,17,7]

def first_challenge(start):
    history = []
    turn = 1
    for num in start:
        turn += 1
        history += [num]
    while turn < 2021:
        if turn % 10000 == 0: print("*")
        if num in history[:-1]:
            index = len(history)-2
            while history[index] != num:
                index -= 1
            num = len(history)-index-1
            history += [num]
        else:
            history += [0]
            num = 0
        turn += 1
    return (history[-1])

def second_challenge(start):
    history={}
    turn = 1
    for x in start:
        history[x] = turn
        turn += 1

    num=start[-1]
    turn = len(start)

    while turn < 30000000:
        if num in history:
            dist = turn - history[num]
            history[num] = turn
            num = dist
        else:
            history[num] = turn
            num = 0
        turn += 1
    return (num)




print('First Challenge test data : ', first_challenge([0,3,6]))
print('First Challenge test data : ', first_challenge([1,3,2]))
print('First Challenge test data : ', first_challenge([2,1,3]))
print('First Challenge test data : ', first_challenge([1,2,3]))
print('First Challenge real data : ', first_challenge( data ))


print()
print('Second Challenge test data : ', second_challenge(   [0,3,6]     ))
print('Second Challenge test data : ', second_challenge(   [1,3,2]     ))
print('Second Challenge real data : ', second_challenge(   data     ))
