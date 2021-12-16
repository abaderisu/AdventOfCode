#!/usr/bin/env python3

import sys

depth = 0
horiz = 0
with open('input.txt') as f:
    for line in f.readlines():
        command = line.strip().split()
        if command[0] == 'forward':
            horiz += int(command[1])
        elif command[0] == 'up':
            depth -= int(command[1])
        elif command[0] == 'down':
            depth += int(command[1])
        else:
            print('Unknown command "' + command[0] + '"')

print(depth * horiz)

