#!/usr/bin/env python3

import re

p = re.compile( '(?=.*byr:(?P<byr>(19[2-9]\d|200[0-2]))(\s|\Z))'
                '(?=.*hgt:(?P<hgt>((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in))(\s|\Z))'
                '(?=.*pid:(?P<pid>\d{9})(\s|\Z))'
                '(?=.*ecl:(?P<ecl>(amb|blu|brn|gry|grn|hzl|oth))(\s|\Z))'
                '(?=.*eyr:(?P<eyr>(202\d|2030))(\s|\Z))'
                '(?=.*hcl:#(?P<hcl>[0-9a-f]{6})(\s|\Z))'
                '(?=.*iyr:(?P<iyr>(201\d|2020))(\s|\Z))')

lines = [line.strip() for line in open('input.txt')]

def splitter(lines):
    string = ''
    for line in lines:
        if line == '':
            yield string
            string = ''
        else:
            string = string + ' ' + line

passports = [pairs for pairs in splitter(lines)]
print(sum([1 if p.match(passport) else 0 for passport in passports]))
