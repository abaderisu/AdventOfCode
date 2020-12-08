#!/usr/bin/env python3

instructions = [line.strip().split(' ') for line in open('input.txt')]
i = 0
visited = set()
accum = 0
while ( i not in visited ):
    visited.add( i )

    if instructions[i][0] == 'acc':
        accum += int(instructions[i][1])
        i += 1
    elif instructions[i][0] == 'jmp':
        i += int(instructions[i][1])
    else:
        i += 1
print(accum)
