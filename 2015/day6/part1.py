#!/usr/bin/env python3

from parse import compile

p = compile('{command} {x1:d},{y1:d} through {x2:d},{y2:d}')

grid = [[False] * 1000 for i in range(1000)]
for instruction in [p.parse(line.strip()) for line in open('input.txt')]:
    command = instruction['command']
    for x in range(instruction['x1'], instruction['x2'] + 1):
        for y in range(instruction['y1'], instruction['y2'] + 1):
            if command == 'turn on':
                grid[y][x] = True
            elif command == 'turn off':
                grid[y][x] = False
            elif command == 'toggle':
                grid[y][x] = not grid[y][x]

print(sum([row.count(True) for row in grid]))
