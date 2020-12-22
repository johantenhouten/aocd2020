#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:55:43 2020

@author: johan
"""


from aocd import get_data
data =get_data(day=18).split('\n')

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def calculate_first(inputstring):
    accumulator = 0
    operator = '+'
    for t in inputstring.split():

        if isInt(t):
            if operator == '+':
                accumulator += int(t)
            elif operator == '*':
                accumulator *= int(t)
        elif t in ['*' , '+']:
            operator = t
    return str(accumulator)

def calculate_second(inputstring):

    while '+' in inputstring:
        tokens = inputstring.split()
        plus = tokens.index('+')
        inputstring = inputstring.replace ( tokens[plus-1]+ ' '+  tokens[plus] + ' '+  tokens[plus+1] , str(eval( tokens[plus-1]+ ' '+  tokens[plus] + ' '+  tokens[plus+1])) )
    return str(eval(inputstring))


def parse_first(inputstring):
    if '(' not in inputstring:
        return calculate_first(inputstring)
    else:
        replacements = []
        for index,char in enumerate(inputstring):
            if char == '(':
                next_parenthis = index +1
                while inputstring[next_parenthis] not in [')', '(']:
                    next_parenthis+=1
                if inputstring[next_parenthis] == ')':
                    to_calculate = inputstring[index+1:next_parenthis]
                    replacements.append (to_calculate)

        for replacement in replacements:
            inputstring = inputstring.replace('('+replacement+')', calculate_first(replacement))
        return parse_first(inputstring)

def parse_second(inputstring):
    if '(' not in inputstring:
        return calculate_second(inputstring)
    else:
        replacements = []
        for index,char in enumerate(inputstring):
            if char == '(':
                next_parenthis = index +1
                while inputstring[next_parenthis] not in [')', '(']:
                    next_parenthis+=1
                if inputstring[next_parenthis] == ')':
                    to_calculate = inputstring[index+1:next_parenthis]
                    replacements.append (to_calculate)

        for replacement in replacements:
            inputstring = inputstring.replace('('+replacement+')', calculate_second(replacement))
        return parse_second(inputstring)


def first_challenge(data):
    result = 0
    for line in data:
        result += int(parse_first(line))
    return(result)

def second_challenge(data):
    result = 0
    for line in data:
        result += int(parse_second(line))
    return(result)

print('First challenge test data ', first_challenge(['1 + 2 * 3 + 4 * 5 + 6']))
print('First challenge test data ', first_challenge(['1 + (2 * 3) + (4 * (5 + 6))']))
print('First challenge test data ', first_challenge(['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']))
print('First challenge real data ', first_challenge(data))

print('Second challenge test data ', second_challenge(['1 + 2 * 3 + 4 * 5 + 6']))
print('Second challenge test data ', second_challenge(['1 + (2 * 3) + (4 * (5 + 6))']))
print('Second challenge test data ', second_challenge(['2 * 3 + (4 * 5)']))
print('Second challenge test data ', second_challenge(['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))']))
print('Second challenge test data ', second_challenge(['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']))
print('Second challenge test data ', second_challenge(data))

