#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:37:01 2020

@author: johan
"""
import string


from aocd import get_data
adventraw = get_data(day=4)
adventraw = adventraw.replace('\n\n', '|')
adventraw = adventraw.replace('\n', ' ')
adventdata=adventraw.split('|')





testraw ='''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''

testraw = testraw.replace('\n\n', '|')
testraw = testraw.replace('\n', ' ')
testdata=testraw.split('|')




def validate_passport1(record):
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
    return ('byr:' in record and 'iyr:' in record and 'eyr:' in record and 'hgt:' in record
    and 'hcl:' in record and 'ecl:' in record and  'pid:' in record )



def validate_passport2(record):
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

    valid = True
    fields = record.split(' ')

    for field_data in fields:
        field, data = field_data.split(':')

        if field == 'byr':
            valid = valid and len(data)==4 and int(data)>=1920 and int(data)<=2002

        elif field == 'iyr':
            valid = valid and len(data)==4 and int(data)>=2010 and int(data)<=2020

        elif field == 'eyr':
            valid = valid and len(data)==4 and int(data)>=2020 and int(data)<=2030

        elif field == 'hgt':
            if 'cm' in data:
                data = data.replace('cm', '')
                valid = valid and int(data) >= 150 and int(data) <= 193
            elif 'in' in data:
                data = data.replace('in','')
                valid = valid and int(data) >= 59 and int(data) <= 76
            else:
                valid = False

        elif field == 'hcl':
            if data[0] != '#':
                valid = False
            data = data[1:]
            valid = valid and all(c in string.hexdigits for c in data)
        elif field == 'ecl':
            valid = valid and data in ['amb', 'blu', 'brn', 'gry' ,'grn', 'hzl', 'oth']
        elif field == 'pid':
            valid = valid and len(data) == 9 and all(c in string.digits for c in data)
        elif field == 'cid':
            valid = valid



    return (valid and 'byr:' in record and 'iyr:' in record and 'eyr:' in record and 'hgt:' in record
    and 'hcl:' in record and 'ecl:' in record and  'pid:' in record )



good = 0
for rec in testdata:
    if validate_passport1(rec): good += 1
good = 0
for r in adventdata:
    if validate_passport1(r) == True:
        good += 1
print('phase 1 ', good)

testraw2 = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''
testraw2 = testraw2.replace('\n\n', '|')
testraw2 = testraw2.replace('\n', ' ')
testdata2=testraw2.split('|')

for rec in testdata2:
    validate_passport2(rec)

good = 0
for rec in adventdata:
    if validate_passport2(rec):
        good += 1
print('Phase 2 ', good)

