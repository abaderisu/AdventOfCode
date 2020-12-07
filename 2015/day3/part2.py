#!/usr/bin/env python3

import sys

def move(x,y,c):
    if c[0] == '>':
        x+=1
    elif c[0] == '<':
        x-=1
    elif c[0] == '^':
        y+=1
    elif c[0] == 'v':
        y-=1
    return x,y

with open(sys.argv[1]) as f:
    coords=[(0,0)]*2
    grid = {}
    grid[0,0] = 1
    while (c := f.read(2)):
        for i in range(0,len(c)):
            coords[i] = move(coords[i][0], coords[i][1], c[i])
            if coords[i] in grid:
                grid[coords[i]] += 1
            else:
                grid[coords[i]] = 1

    print(len(grid.keys()))
