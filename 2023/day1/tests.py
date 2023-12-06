#!/usr/bin/env python3

from day1 import parseCal,parseCalDoc

assert parseCal('1abc2',False) == 12,parseCal('1abc2',False)
assert parseCal('pqr3stu8vwx',False) == 38
assert parseCal('a1b2c3d4e5f',False) == 15
assert parseCal('treb7uchet',False) == 77

lines = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

cal = parseCalDoc(lines.split(),False)
assert cal == 142,cal

lines = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''

cal = parseCalDoc(lines.split(),True)
assert cal == 281,cal
