#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 22:13:28 2020

@author: johan
"""

from aocd import get_data
message = get_data(day=9).split('\n')
message = [ int(x) for  x in message]

def validateXMAS(character, preamblelist):
    for x in preamblelist:
        if character-x in preamblelist:
            return True
    return False


testdata="""35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split('\n')
testdata = [ int(x) for  x in testdata]
preamble=5



character = preamble
while validateXMAS(testdata[character], testdata[character-preamble:character]):
    character +=1
print('Phase 1 - testdata ', testdata[character])




preamble=25
character = preamble
while validateXMAS(message[character], message[character-preamble:character]):
    character +=1
print('Phase 1 - realdata ', message[character])




for start in range(len(testdata)):
    for end in range(start+1,  len(testdata)):
        if sum(testdata[start:end])==127 and (end-start)>1:
            print('Phase 2 testdata ', testdata[start:end], min(testdata[start:end]) + max(testdata[start:end]))



for start in range(len(message)):
    for end in range(start+1,  len(message)):
        if sum(message[start:end])==14360655 and (end-start)>1:
            print('Phase 2 challenge ', message[start:end], min(message[start:end]) + max(message[start:end]))


