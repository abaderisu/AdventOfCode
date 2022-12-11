#!/usr/bin/env python3

part1_rules = {'A':{'X':3,'Y':6,'Z':0},'B':{'X':0,'Y':3,'Z':6},'C':{'X':6,'Y':0,'Z':3}}
part2_rules = {'A':{'X':(0,'C'),'Y':(3,'A'),'Z':(6,'B')},'B':{'X':(0,'A'),'Y':(3,'B'),'Z':(6,'C')},'C':{'X':(0,'B'),'Y':(3,'C'),'Z':(6,'A')}}

part1_score = 0
part2_score = 0
input = [line.split() for line in open('input.txt').readlines()]
for pair in input:
    part1_score += part1_rules[pair[0]][pair[1]] + (ord(pair[1]) - ord('W'))
    part2_move = part2_rules[pair[0]][pair[1]]
    part2_score += part2_move[0] + (ord(part2_move[1]) - 64)

print('Part 1',part1_score)
print('Part 2',part2_score)
