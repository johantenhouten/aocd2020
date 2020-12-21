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



def parse_data(inputdata):
    data = copy.deepcopy(inputdata)
    line = data.pop(0)
    rules = {}
    while line != '':
        rule,value_list = line.split(': ')
        values = []
        for value_range in value_list.split(' or '):
            values += list(range( int(value_range.split('-')[0]) , int(value_range.split('-')[1])+1 ) )
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



rules,myticket,nearby = parse_data(data)


invalid = []
for ticket in nearby:
    for value in ticket:
        count = 0
        for rule in rules:
            if value in rules[rule]:
                count +=1
        if count == 0:
            invalid.append(ticket)
for ticket in invalid:
    nearby.remove(ticket)


result = {}
columns = list(range(len(rules)))
for i in range(20):
    for rule in rules:
        count = 0
        for colnum in columns:
            col = [c[colnum] for c in nearby]
            if (len( [v for v in [ c[colnum] for c in nearby] if v in rules[rule]]) == len (nearby)):
                count += 1
                one_rule = rule
                one_col = colnum
        if count == 1:
            result[one_rule] = one_col
            del rules[one_rule]
            columns.remove(one_col)
            break

answer = 1
for rule in result:
    if 'departure' in rule:
        print(rule, result[rule])
        answer *= myticket[result[rule]]

print('Second challenge answer: ',answer)