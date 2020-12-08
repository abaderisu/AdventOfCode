#!/usr/bin/env python3

import copy

def run(instructions):
    i = 0
    visited = set()
    accum = 0
    while i not in visited and i < len(instructions):

        visited.add( i )

        if instructions[i][0] == 'acc':
            accum += int(instructions[i][1])
            i += 1
        elif instructions[i][0] == 'jmp':
            i += int(modified[i][1])
        elif instructions[i][0] == 'nop':
            i += 1
        else:
            print('invalid instruction ' + instructions[i][0])
    
    return (i,accum)

instructions = [line.strip().split(' ') for line in open('input.txt')]

for i in range(0,len(instructions)):
    modified = copy.deepcopy(instructions)

    if modified[i][0] == 'jmp':
        modified[i][0] = 'nop'
    elif modified[i][0] == 'nop':
        modified[i][0] = 'jmp'
    else:
        continue
    
    final = run(modified)
    if  final[0] >= len(modified):
        print(final[1])
        break
