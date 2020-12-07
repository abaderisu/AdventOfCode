#!/usr/bin/env python3

import sys

floor = 0
with open(sys.argv[1]) as f:
    for c in f.read():
        if c == '(':
            floor +=1
        elif c == ')':
            floor -= 1

print(floor)
