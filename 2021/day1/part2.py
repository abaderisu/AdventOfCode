#!/usr/bin/env python3

import sys
import collections

increases = 0
prev = None
windowa = collections.deque(maxlen=3)
windowb = collections.deque(maxlen=3)

with open('input.txt') as f:
    for line in f.readlines():
        depth = int(line.strip())
        windowa.append(depth)
        if len(windowa) > 1:
            windowb.append(depth)
        if prev is not None:
            total = sum(windowb)
            if total > prev:
                increases += 1
        if len(windowa) == 3:
            prev = sum(windowa)

print(increases)
