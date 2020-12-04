#!/usr/bin/env python3

import re

p = re.compile('(?=.*eyr:\S+)(?=.*hgt:\S+)(?=.*pid:\S+)(?=.*ecl:\S+)(?=.*byr:\S+)(?=.*hcl:\S+)(?=.*iyr:\S+)')
passports = ['']
lines = [line.strip() for line in open('input.txt')]
for line in lines:
    if line == '':
        passports.append('')
    else:
        passports[len(passports) - 1] = passports[len(passports) - 1] + ' ' + line

print(sum([1 if p.match(passport) else 0 for passport in passports]))
