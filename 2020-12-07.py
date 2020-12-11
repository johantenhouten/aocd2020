#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 22:20:32 2020

@author: johan
"""


from aocd import get_data
all_rules = get_data(day=7).split('\n')


example ="""light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".splitlines()


example2="""shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""".splitlines()

def extract_bags(bags_inside):
    if bags_inside == 'no other bags.':
        return []
    else:
        results = bags_inside.split(',')
        for index in range(len(results)):
            results[index] = results[index].replace('.','')
            results[index] = results[index].replace('bags','')
            results[index] = results[index].replace('bag','')
            results[index] = results[index].strip()
            results[index] = results[index][2:]
    return results

def gold_inbag(list_of_bags):
    if list_of_bags == []:
        return False
    elif 'shiny gold' in list_of_bags :
        return True
    elif len(list_of_bags) == 1:
        return gold_inbag(rules[list_of_bags[0]])
    else:
        split = len(list_of_bags)//2
        return gold_inbag(list_of_bags[:split]) or  gold_inbag(list_of_bags[split:])

def updaterules(bag, replacetext):
    for rule in rules:
        if bag in str(rules[rule]) :
            rules[rule] = rules[rule].replace(bag, '*' + str(replacetext))
    return



rules = {}
count = 0
for rule in example:
    bag, bags_inside  = rule.split(' contain ')
    bag = bag.replace('bags','')
    bag = bag.replace('bag','')
    bag = bag.strip()
    rules[bag] = extract_bags(bags_inside)
for bag in rules:
    count += 1
print('Example data count   : ', count)

rules = {}
count = 0
for rule in all_rules:
    bag, bags_inside  = rule.split(' contain ')
    bag = bag.replace('bags','')
    bag = bag.replace('bag','')
    bag = bag.strip()
    rules[bag] = extract_bags(bags_inside)
for bag in rules:
    if gold_inbag(rules[bag]):
        count+=1
print('Challenge 1 count    :', count)




print('\n\nPart 2')
rules = {}
for rule in example:
    rule = rule.replace(' bags','')
    rule = rule.replace(' bag','')
    rule = rule.replace('.','')
    rule = rule.replace(',',' +')

    bag, contents = rule.split(' contain ')
    if contents == 'no other':
        contents = 1
    else:
        contents = '1 + ' + contents
    rules[bag] = contents
done = False
while type(rules['shiny gold']) != int:
    done = True
    for rule in rules:
        if type(rules[rule]) == int:
            updaterules(rule, rules[rule])
    for rule in rules:
        try:
            eval(rules[rule])
        except:
            done =False
        else:
            rules[rule] = eval(rules[rule])
print('Phase 2 - exampe 1 -> a shiny gold bag contains ', rules['shiny gold'] - 1, ' bags.')

rules = {}
for rule in example2:
    rule = rule.replace(' bags','')
    rule = rule.replace(' bag','')
    rule = rule.replace('.','')
    rule = rule.replace(',',' +')

    bag, contents = rule.split(' contain ')
    if contents == 'no other':
        contents = 1
    else:
        contents = '1 + ' + contents
    rules[bag] = contents
done = False
while type(rules['shiny gold']) != int:
    done = True
    for rule in rules:
        if type(rules[rule]) == int:
            updaterules(rule, rules[rule])
    for rule in rules:
        try:
            eval(rules[rule])
        except:
            done =False
        else:
            rules[rule] = eval(rules[rule])
print('Phase 2 - exampe 2 -> a shiny gold bag contains ', rules['shiny gold'] - 1, ' bags.')


rules = {}
for rule in all_rules:
    rule = rule.replace(' bags','')
    rule = rule.replace(' bag','')
    rule = rule.replace('.','')
    rule = rule.replace(',',' +')

    bag, contents = rule.split(' contain ')
    if contents == 'no other':
        contents = 1
    else:
        contents = '1 + ' + contents
    rules[bag] = contents
done = False
while type(rules['shiny gold']) != int:
    done = True
    for rule in rules:
        if type(rules[rule]) == int:
            updaterules(rule, rules[rule])
    for rule in rules:
        try:
            eval(rules[rule])
        except:
            done =False
        else:
            rules[rule] = eval(rules[rule])
print('Phase 2 - challege -> a shiny gold bag contains ', rules['shiny gold'] - 1, ' bags.')

