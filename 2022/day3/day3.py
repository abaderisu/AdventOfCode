#!/usr/bin/env python3

def priority(c):
    if c.isupper():
        return ord(c) - ord('A') + 27
    else:
        return ord(c) - ord('a') + 1

def calc_part1(sack):
    pocket1 = sack[:len(sack)//2]
    pocket2 = sack[len(sack)//2:]
    dupe = set(pocket1).intersection(set(pocket2)).pop()
    return priority(dupe)

def calc_part2(group):
    dupe = group[0].intersection(group[1]).intersection(group[2]).pop()
    return priority(dupe)

group = []
part1_priority = 0
part2_priority = 0
for line in open('input.txt').readlines():
    line = line.strip()
    part1_priority += calc_part1(line)

    group.append(set(line))
    if len(group) == 3:
        part2_priority += calc_part2(group)
        group.clear()

print('Part 1',part1_priority)
print('Part 2',part2_priority)
