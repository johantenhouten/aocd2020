#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: johan
"""



from aocd import get_data
tickets = get_data(day=5).split('\n')

def getseatID(ticket):
    row=ticket[0:7].replace('F','0').replace('B','1')
    row =int(row,2)
    seat=ticket[7:].replace('L','0').replace('R','1')
    seat=int(seat,2)
    ID = row*8+seat
    return(ID)


ticket='FBFBBFFRLR'
print('SeatID test data ', getseatID(ticket))

print('Max seatID in plane ',  max([getseatID(ticket) for ticket in tickets ] ))


seatIDS = [getseatID(ticket) for ticket in tickets ]

for i in range(1,max(seatIDS)-1):
    if i-1 in seatIDS and i+1 in seatIDS and i not in seatIDS:
        print('Seat ', i)
