#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:06:03 2020

@author: johan
"""

import copy
from aocd import get_data
challenge_waitingarea_data = get_data(day=11).split('\n')

test_waitingarea_data="""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".split('\n')

def adjacent_occupied_seats(waitingarea,row,col):
    height = len(waitingarea)
    width = len(waitingarea[0])
    number_occupied_seats = 0

    for dRow in [-1,0,1]:
        for dCol in [-1,0,1]:
            if row+dRow >= 0 and row+dRow < height and col+dCol >= 0 and col+dCol<width and not (dRow ==0 and dCol==0):
                if waitingarea[row+dRow][col+dCol] == '#':
                    number_occupied_seats +=1
    return number_occupied_seats

def adjacent_visible_seats(waitingarea,seatrow,seatCol):
    height = len(waitingarea)
    width = len(waitingarea[0])

    number_visible_seats = 0
    for dRow,dCol in [ (-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1),(1,0), (1,1)]:
        row = seatrow
        col = seatCol
        while row+dRow >= 0 and row+dRow < height and col+dCol >= 0 and col+dCol<width :
            if waitingarea[row+dRow][col+dCol] == '#' :
                number_visible_seats +=1
                break
            if waitingarea[row+dRow][col+dCol] == 'L' :
                break
            row += dRow
            col += dCol

    return number_visible_seats

def count_occupied_seats(waitingarea):
    height = len(waitingarea)
    width = len(waitingarea[0])
    count = 0
    for row in range(height):
        for col in range(width):
            if waitingarea[row][col] == '#':
                count +=1
    return count

def iterate_adjacent(waitingarea):
    height = len(waitingarea)
    width = len(waitingarea[0])
    next_waitingarea = copy.deepcopy(waitingarea)
    swaps = 0
    for row in range(height):
        for col in range(width):
            if waitingarea[row][col] == 'L' and adjacent_occupied_seats(waitingarea,row,col) == 0:
                next_waitingarea[row][col] = '#'
                swaps += 1
            elif waitingarea[row][col] == '#' and adjacent_occupied_seats(waitingarea,row,col) >= 4:
                swaps += 1
                next_waitingarea[row][col] = 'L'
            else:
                next_waitingarea[row][col] = waitingarea[row][col]
    return swaps, next_waitingarea

def iterate_visible(waitingarea):
    height = len(waitingarea)
    width = len(waitingarea[0])
    next_waitingarea = copy.deepcopy(waitingarea)
    swaps = 0
    for row in range(height):
        for col in range(width):
            if waitingarea[row][col] == 'L' and adjacent_visible_seats(waitingarea,row,col) == 0:
                next_waitingarea[row][col] = '#'
                swaps += 1
            elif waitingarea[row][col] == '#' and adjacent_visible_seats(waitingarea,row,col) >= 5:
                swaps += 1
                next_waitingarea[row][col] = 'L'
            else:
                next_waitingarea[row][col] = waitingarea[row][col]
    return swaps, next_waitingarea

def printmap(waitingarea):
    height = len(waitingarea)
    width = len(waitingarea[0])
    for row in range(height):
        for col in range(width):
            print(waitingarea[row][col], end= '')
        print()
    print()

def first_challenge(waitingarea_data):
    waitingarea = []
    for row in waitingarea_data:
        waitingarea.append([c for c in row])
    swaps = 1
    while swaps > 0:
        swaps, waitingarea = iterate_adjacent(waitingarea)
    print('chaos has stabilized')
    printmap(waitingarea)
    return count_occupied_seats(waitingarea)

def second_challenge(waitingarea_data):
    waitingarea = []
    for row in waitingarea_data:
        waitingarea.append([c for c in row])
    swaps = 1
    while swaps > 0:
        swaps, waitingarea = iterate_visible(waitingarea)
    return count_occupied_seats(waitingarea)


#print("\nFirst test data stabalizes, and there are ", first_challenge(test_waitingarea_data), " seats occupied.")
#print("\nFirst challenge data stabalizes, and there are ", first_challenge(challenge_waitingarea_data), " seats occupied.")


# printmap(test_waitingarea_data)
# waitingarea = []
# for row in test_waitingarea_data:
#     waitingarea.append([c for c in row])

# for i in range(27):
#     swaps, waitingarea = iterate_visible(waitingarea)
#     printmap(waitingarea)

# print(swaps)
# print(count_occupied_seats(waitingarea))

print("\nSeond test data stabalizes, and there are ", second_challenge(test_waitingarea_data), " seats occupied.")
print("\nSeond challenge data stabalizes, and there are ", second_challenge(challenge_waitingarea_data), " seats occupied.")
