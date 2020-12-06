#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 13:05:41 2020

@author: johan
"""
import string

from aocd import get_data
all_responses = get_data(day=6).split('\n\n')

test = """abc

a
b
c

ab
ac

a
a
a
a

b"""


test_responses = test.split('\n\n')


def count_yes(group_response_list):
    count = 0
    for group_response in group_response_list:
        group_customs_declaration_form = ''
        for individual_customs_declaration_form in group_response.split('\n'):
            for answer in individual_customs_declaration_form:
                if answer not in group_customs_declaration_form:
                    group_customs_declaration_form += answer
        count +=len(group_customs_declaration_form)
    return count

def count_all_yes(group_response_list):
    count = 0
    for group_response in group_response_list:
        group_customs_declaration_form = [char for char in string.ascii_lowercase ]
        for individual_customs_declaration_form in group_response.split('\n'):
            individual_customs_declaration_answers = [c for c in individual_customs_declaration_form]
            group_customs_declaration_form = [ answer for answer in  group_customs_declaration_form if answer in individual_customs_declaration_answers ]
        count += len(group_customs_declaration_form)
    return(count)



print('Test data ', count_yes(test_responses))
print('Challenge data ', count_yes(all_responses))

print("\n\nPart 2 ")

print('Test data ',count_all_yes(test_responses))
print('Challenge data ', count_all_yes(all_responses))

