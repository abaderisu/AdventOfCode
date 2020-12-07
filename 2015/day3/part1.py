#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    x = 0
    y = 0
    grid = {}
    grid[x,y] = 1
    for c in f.read():
        if c == '>':
            x+=1
        elif c == '<':
            x-=1
        elif c == '^':
            y+=1
        elif c == 'v':
            y-=1

        if (x,y) in grid:
            grid[x,y] += 1
        else:
            grid[x,y] = 1

    print(len(grid.keys()))
