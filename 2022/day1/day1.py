#!/usr/bin/env python3

top_elves = [0,0,0]
cals = 0

input = [line.strip() for line in open('input.txt').readlines()]
for i in range(len(input)):
    if input[i] == '' or i == len(input) - 1:
        top_elves.append(cals)
        top_elves.remove(min(top_elves))
        cals = 0
    else:
        cals += int(input[i])

print('Part 1:', max(top_elves))
print('Part 2:', sum(top_elves))
