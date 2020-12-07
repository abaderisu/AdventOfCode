#!/usr/bin/env python3

import sys

floor = 0
basement = 0
with open(sys.argv[1]) as f:
    for c in f.read():
        if c == '(':
            floor +=1
        elif c == ')':
            floor -= 1
        
        basement += 1
        if floor == -1:
            break
print(basement)
