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
        val = max([l, w, h])
        if val == l:
            total += 2*w + 2*h
        elif val == w:
            total += 2*l + 2*h
        else:
            total += 2*l + 2*w

        total += l * w * h

print(total) 
