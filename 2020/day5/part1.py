#!/usr/bin/env python3

import re

lines = [line.strip() for line in open('input.txt')]
ids = []
for line in lines:
    rmin = 0
    rmax = 127
    for i in range(0,7):
        half = int(64 / (1 << i))
        if line[i] == 'F':
            rmax -= half
        else:
            rmin += half
    cmin = 0
    cmax = 7
    for i in range(0,3):
        half = int(4 / (1 << i))
        if line[i + 7] == 'L':
            cmax -= half
        else:
            cmin += half
    ids.append(rmin * 8 + cmin)
print(max(ids))
