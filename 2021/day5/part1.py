#!/usr/bin/env python3

import re

lines = [[int(e) for e in re.findall('\d+',line.strip())] for line in open('input.txt')]
maxx = max([e for line in lines for e in (line[0],line[2])])
maxy = max([e for line in lines for e in (line[1],line[3])])
grid = [[0 for i in range(maxx)] for j in range(maxy)]

for (x1,y1,x2,y2) in lines:
    if x1 != x2 and y1 != y2:
        continue
    if x1 != x2:
        for x in range(min(x1,x2),max(x1,x2)+1):
            grid[y1][x] += 1
    if y1 != y2:
        for y in range(min(y1,y2),max(y1,y2)+1):
            grid[y][x1] += 1


total = sum([sum([1 for e in row if e > 1]) for row in grid])
print(total)
