#!/usr/bin/env python3

import sys
from parse import compile

p = compile('{l:d}x{w:d}x{h:d}')

total = 0
with open(sys.argv[1]) as f:
    for line in f.readlines():
        parsed = p.parse(line)
        l = parsed['l']
        w = parsed['w']
        h = parsed['h']
        areas = [2*l*w, 2*w*h, 2*h*l]
        total += sum(areas) + (min(areas) / 2)
print(total) 
