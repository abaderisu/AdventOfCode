#!/usr/bin/env python3

import sys
from parse import compile

p = compile('{first:d}-{second:d} {char}: {password}')

valid = 0
with open(sys.argv[1]) as f:
    for line in f.readlines():
        parsed = p.parse(line)
        password = parsed['password']
        first = password[parsed['first'] - 1] == parsed['char']
        second = password[parsed['second'] - 1] == parsed['char']
        if first ^ second:
            valid+=1
       
print(valid) 
