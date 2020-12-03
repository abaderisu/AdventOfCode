#!/usr/bin/env python3

import sys

terrain = []
with open(sys.argv[1]) as f:
    for line in f.readlines():
        terrain.append( line.strip() )

x = 0
y = 0
trees = 0
while True:
    x += 3
    y += 1
    if y >= len(terrain):
        break
    if terrain[y][x % len(terrain[0])] == '#':
        trees += 1

print(trees)
