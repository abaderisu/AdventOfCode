#!/usr/bin/env python3

from day12 import fillTerrain,walkPath

lines = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''

terrain,start,end = fillTerrain(lines.split('\n'))
assert start == (0,0),start
assert end == (5,2),end

trails = walkPath(terrain,end)
assert trails[start] == 31,dists
assert min([d for d in trails.values()]) == 29
