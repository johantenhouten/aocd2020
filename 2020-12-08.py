#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:05:38 2020

@author: johan
"""

from copy import deepcopy


from aocd import get_data
mem = get_data(day=8).split('\n')




def test_infinite_loop(memory, inspect):
    mem = deepcopy(memory)

    if 'jmp' in mem[inspect]:
        mem[inspect] = mem[inspect].replace('jmp', 'nop')
    elif 'nop' in mem[inspect]:
        mem[inspect] = mem[inspect].replace('nop', 'jmp')


    ip = 0
    acc = 0
    while ip>=0 and ip < len(mem) and mem[ip] != 'x' :
        opcode, argument = mem[ip].split()
        argument= int(argument)
        if opcode == 'acc':
            acc += argument
            mem[ip] = 'x'
            ip +=1
        elif opcode == 'jmp':
            mem[ip] = 'x'
            ip += argument
        elif opcode == 'nop':
            mem[ip] = 'x'
            ip +=1
    if ip >= len(mem):
        print('yeah finishes', acc)







ip = 0
acc = 0
while mem[ip] != 'x':
    opcode, argument = mem[ip].split()
    if opcode == 'acc':
        acc += int(argument)
        mem[ip] = 'x'
        ip +=1
    if opcode == 'jmp':
        mem[ip] = 'x'
        ip += int(argument)
    if opcode == 'nop':
        mem[ip] = 'x'
        ip +=1
print('first challenge ', acc)




mem = get_data(day=8).split('\n')
for inspect in range(len(mem)):
    test_infinite_loop(mem,inspect)



