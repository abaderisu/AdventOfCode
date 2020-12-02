#!/usr/bin/env python3

import sys
from parse import compile

p = compile('{min:d}-{max:d} {char}: {password}')

valid = 0
with open(sys.argv[1]) as f:
    for line in f.readlines():
        parsed = p.parse(line)
        c = parsed['password'].count(parsed['char'])
        if c >= parsed['min'] and c <= parsed['max']:
            valid+=1
       
print(valid) 
