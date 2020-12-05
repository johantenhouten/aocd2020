#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:37:01 2020

@author: johan
"""
from aocd import get_data
# advent of code day 2
test = ['1-3 a: abcde','1-3 b: cdefg', '2-9 c: ccccccccc']


data = get_data(day=2).split('\n')

good =0
for line in data:
    policy,char,password = line.split()
    char = char[0]
    minchar, maxchar = map(int, policy.split('-'))
    if password.count(char) >= minchar and password.count(char) <= maxchar :
        good += 1
print(good)

#part 2

good =0
for line in data:
    policy,char,password = line.split()
    char = char[0]
    firstchar, secondchar = map(int, policy.split('-'))
    if (password[firstchar-1] == char  and password[secondchar-1] != char) or (password[firstchar-1] != char  and password[secondchar-1] == char):
        good += 1
print(good)
