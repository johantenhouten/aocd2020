#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 14:38:10 2020

@author: johan
"""


from aocd import get_data
import copy



data =get_data(day=16).split('\n')
testdata="""class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12""".split('\n')

testdata2="""class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9""".split('\n')




def parse_data(data):
    line = data.pop(0)
    rules = {}
    while line != '':
        rule,value_list = line.split(': ')
        values = value_list.split(' or ')
        rules[rule] = values
        line = data.pop(0)

    line = data.pop(0)
    myticket = [int(d) for d in data.pop(0).split(',')]
    data.pop(0)
    data.pop(0)

    line = data.pop(0)
    nearby=[]
    while data:
        values = [int(value) for value in line.split(',')]
        nearby.append(values)
        line = data.pop(0)
    values = [int(value) for value in line.split(',')]
    nearby.append(values)



    return rules,myticket,nearby

def first_challenge(data):
    rules,myticket,nearby = parse_data(copy.deepcopy(data))

    result = 0
    for ticket in nearby:
        for value in ticket:
            count = 0
            for rule in rules:

                for ranges in rules[rule]:
                    lower,higher = map(int, ranges.split('-'))
                    if value >= lower and value <= higher:
                        count +=1
            if count == 0:
                result += value
    return result



print('First challenge test data', first_challenge(testdata))
print('First challenge real data', first_challenge(data))


