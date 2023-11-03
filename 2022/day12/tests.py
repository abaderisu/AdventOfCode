#!/usr/bin/env python3

from day12 import fillTerrain,walkPath

lines = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''

terrain,start,end,lows = fillTerrain(lines.split('\n'))
assert start == (0,0),start
assert end == (5,2),end
assert lows == [(0,0),(1,0),(0,1),(0,2),(0,3),(0,4)]

trails = walkPath(terrain,lows,end)
assert trails[start] == 31,dists
assert min([d for d in trails.values()]) == 29
