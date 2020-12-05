#!/usr/bin/env python3

import re

lines = [line.strip() for line in open('input.txt')]
ids = []
for line in lines:
    row = sum([int(64 / (1<<i)) for i in range(0,7) if line[i] == 'B'])
    col = sum([int(4 / (1 << i)) for i in range(0, 3) if line[i + 7] == 'R'])
    ids.append(row * 8 + col)

ids.sort()
for i in range(0,len(ids)):
    if ids[i + 1] != ids[i] + 1:
        print(ids[i] + 1)
        break
