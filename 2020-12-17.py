#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 22:20:09 2020

@author: johan
"""

from aocd import get_data
import copy

data =get_data(day=17).split('\n')


testdata=""".#.
..#
###""".split('\n')


def count_neighbours3D(grid,x,y,z):
    actvies = 0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            for dz in [-1,0,1]:
                if not (dx==0 and dy==0 and dz==0):
                    if (x+dx,y+dy,z+dz) in grid:
                            actvies += 1
    return(actvies)

def count_neighbours4D(grid,x,y,z,w):
    actvies = 0

    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            for dz in [-1,0,1]:
                for dw in [-1,0,1]:
                    if not (dx==0 and dy==0 and dz==0 and dw==0):
                        if (x+dx,y+dy,z+dz,dw+w) in grid:
                                actvies += 1
    return(actvies)


def printGrid3D(grid):
    maxX = max([ x[0] for x in grid])+2
    minX = min([ x[0] for x in grid])-1
    maxY = max([ x[1] for x in grid])+2
    minY = min([ x[1] for x in grid])-1
    maxZ = max([ x[2] for x in grid])+2
    minZ = min([ x[2] for x in grid])-1
    for z in range(minZ, maxZ):
        print('z=%d'% z)
        for x in range(minX,maxX):
            for y in range(minY, maxY):
                if (x,y,z) in grid:
                    print('#',end='')
                else:
                    print('.',end='')
            print()

def first_challenge(data):
    grid = []
    z= 0
    for x, xrow in enumerate(data):
        for y,c in enumerate(xrow):
            if c == '#': grid.append ((x,y,z))
    # data is imported

    for i in range(6):
        next_gen = []
        maxX = max([ x[0] for x in grid])+2
        minX = min([ x[0] for x in grid])-1
        maxY = max([ x[1] for x in grid])+2
        minY = min([ x[1] for x in grid])-1
        maxZ = max([ x[2] for x in grid])+2
        minZ = min([ x[2] for x in grid])-1
        for z in range(minZ, maxZ):
            for x in range(minX,maxX):
                for y in range(minY, maxY):
                    if (x,y,z) in grid:
                        neighbours = count_neighbours3D(grid,x,y,z)
                        # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
                        # Otherwise, the cube becomes inactive.
                        if neighbours == 2 or neighbours == 3:
                            next_gen.append ((x,y,z))
                    elif count_neighbours3D(grid,x,y,z) == 3:
                        next_gen.append((x,y,z))
        grid = copy.deepcopy(next_gen)

    #printGrid3D(grid)

    return len(grid)





def second_challenge(data):
    grid = []
    z= 0
    w=0
    for x, xrow in enumerate(data):
        for y,c in enumerate(xrow):
            if c == '#': grid.append ((x,y,z,w))
    # data is imported

    for i in range(6):
        print(i)
        next_gen = []
        maxX = max([ x[0] for x in grid])+2
        minX = min([ x[0] for x in grid])-1
        maxY = max([ x[1] for x in grid])+2
        minY = min([ x[1] for x in grid])-1
        maxZ = max([ x[2] for x in grid])+2
        minZ = min([ x[2] for x in grid])-1
        maxW = max([ x[3] for x in grid])+2
        minW = min([ x[3] for x in grid])-1

        for w in range(minW,maxW):
            for z in range(minZ, maxZ):
                for x in range(minX,maxX):
                    for y in range(minY, maxY):
                        if (x,y,z,w) in grid:
                            neighbours = count_neighbours4D(grid,x,y,z,w)
                            if neighbours == 2 or neighbours == 3:
                                next_gen.append ((x,y,z,w))
                        elif count_neighbours4D(grid,x,y,z,w) == 3:
                            next_gen.append((x,y,z,w))
        grid = copy.deepcopy(next_gen)


    return len(grid)




#print('First challenge test data : ', first_challenge(testdata))
#print('First challenge real data : ', first_challenge(data))
#print('Second challenge test data : ', second_challenge(testdata))
print('Second challenge rea data : ', second_challenge(data))




