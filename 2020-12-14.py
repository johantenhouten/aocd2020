#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 23:29:25 2020

@author: johan
"""

from aocd import get_data

instructions = get_data(day=14).split('\n')
testdata="""mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".split('\n')

testdata2="""mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""".split('\n')


def first_challenge(data):
    memory = {}
    for line in data:
        if 'mask' in line:
            mask = line
        if 'mem[' in line:
            address = int(line.split()[0][4:][:-1])
            value = int(line.split()[2])      # mem[x] =  xxxx -> 3rd word
            binmem = f"{int(value):#038b}"[2:] # int to bits and drop leading 0b
            binmask = mask.split()[2]
            result = ''
            for index,maskchar  in enumerate(binmask):
                if maskchar == 'X':
                    result = result + binmem[index]
                else:
                    result = result +maskchar
            memory[address] = int(result,2)

    return sum([memory[m] for m in memory])


def second_challenge(data):
    memory = {}
    for line in data:
        if 'mask' in line:
            mask = line
        if 'mem[' in line:
            bitmask = mask.split()[2]
            address = int(line.split()[0][4:][:-1])
            binaddress = f"{int(address):#038b}"[2:]
            value = int(line.split()[2])
            maskedaddress = ''
            for index,bit  in enumerate(bitmask):
                if bit == '0':
                    maskedaddress= maskedaddress + binaddress[index]
                elif bit == '1':
                    maskedaddress= maskedaddress + '1'
                else:
                    maskedaddress= maskedaddress + 'X'
            addresses = [maskedaddress]
            done = False
            while not done:
                done = True
                for address in addresses:
                    if 'X' in address:
                        addresses.remove(address)
                        addresses.append(address.replace('X','1',1)) # reaplce only 1 char
                        addresses.append(address.replace('X','0',1)) # reaplce only 1 char
                        done = False

            for a in addresses:
                memory[int(a,2)] = value

    return sum([memory[cel] for cel in memory])



#print('first challenge test data: ', first_challenge(testdata))
#print('first challenge real data: ', first_challenge(instructions))

print('second challenge test data: ', second_challenge(testdata2))
print('second challenge real data: ', second_challenge(instructions))

