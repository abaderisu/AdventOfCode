#!/usr/bin/env python3

import math
import sys

def sled(terrain, slope):
    trees = 0
    x = slope[0]
    y = slope[1]
    while y < len(terrain):
        if terrain[y][x % len(terrain[0])] == '#':
            trees += 1
        x += slope[0]
        y += slope[1]
    print(trees)
    return trees

terrain = [line.strip() for line in open(sys.argv[1])]

trees = []
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
for slope in slopes:
    trees.append(sled(terrain,slope))
print(math.prod(trees))
