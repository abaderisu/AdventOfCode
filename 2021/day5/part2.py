#!/usr/bin/env python3

import re

lines = [[int(e) for e in re.findall('\d+',line.strip())] for line in open('input.txt')]
maxx = max([e for line in lines for e in (line[0],line[2])])
maxy = max([e for line in lines for e in (line[1],line[3])])
grid = [[0 for i in range(maxx + 1)] for j in range(maxy + 1)]

for (x1,y1,x2,y2) in lines:
    xstep = 1 if x2 > x1 else -1
    ystep = 1 if y2 > y1 else -1
    xs = [e for e in range(x1,x2+xstep,xstep)]
    ys = [e for e in range(y1,y2+ystep,ystep)]

    if len(xs) == 1:
        for y in ys:
            grid[y][xs[0]] += 1
    elif len(ys) == 1:
        for x in xs:
            grid[ys[0]][x] += 1
    else:
        for x,y in zip(xs,ys):
            grid[y][x] += 1

total = sum([sum([1 for e in row if e > 1]) for row in grid])
print(total)
