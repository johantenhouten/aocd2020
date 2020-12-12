#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:49:13 2020

@author: johan
"""

from aocd import get_data
import math

adapters_data = get_data(day=10).split('\n')

testadapters_data="""16
10
15
5
1
11
7
19
6
12
4""".split('\n')

testadapters_data2 ="""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".split('\n')



def count_jolts(data):
    adapters = [int(adapter) for adapter in data]
    effective_joltage_rating = 0
    built_in_adapter = max(adapters)+3
    adapters.append(effective_joltage_rating)
    adapters.append(built_in_adapter)
    adapters.sort()
    diffs = [0,0,0,0]
    for index in range(1,len(adapters)):
        diff = adapters[index] - adapters[index-1]
        diffs[diff] +=1

    return diffs

def max_consecutive_jolts(data):
    adapterlist = [int(d) for  d in data]
    adapterlist.sort()
    consecutive_jolts = {0:1}
    for adapter in adapterlist:
        consecutive_jolts[adapter] = 0
        if adapter - 1 in consecutive_jolts:
            consecutive_jolts[adapter]+=consecutive_jolts[adapter-1]
        if adapter - 2 in consecutive_jolts:
            consecutive_jolts[adapter]+=consecutive_jolts[adapter-2]
        if adapter - 3 in consecutive_jolts:
            consecutive_jolts[adapter]+=consecutive_jolts[adapter-3]
    return (consecutive_jolts[max(adapterlist)])


print('Test data 1    ', count_jolts(testadapters_data), ' -->' ,count_jolts(testadapters_data)[1]*count_jolts(testadapters_data)[3])
print('Test data 2    ', count_jolts(testadapters_data2), ' -->' ,count_jolts(testadapters_data2)[1]*count_jolts(testadapters_data2)[3])
print('Challenge data ', count_jolts(adapters_data), ' -->' ,count_jolts(adapters_data)[1]*count_jolts(adapters_data)[3])



print("\n\n===========================================\n\n")

print('Test data 1    ', max_consecutive_jolts(testadapters_data), ' --> 8')
print('Test data 2    ', max_consecutive_jolts(testadapters_data2), ' -->' ,19208)
print('Challenge data data 2    ', max_consecutive_jolts(adapters_data))

