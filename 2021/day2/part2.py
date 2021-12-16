#!/usr/bin/env python3

import sys

aim = 0
depth = 0
horiz = 0
with open('input.txt') as f:
    for line in f.readlines():
        command = line.strip().split()
        value = int(command[1])
        if command[0] == 'forward':
            horiz += value
            depth += value * aim
        elif command[0] == 'up':
            aim -= value
        elif command[0] == 'down':
            aim += value
        else:
            print('Unknown command "' + command[0] + '"')

print(depth * horiz)

