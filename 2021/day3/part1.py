#!/usr/bin/env python3

totals = None
with open('input.txt') as f:
    for line in f.readlines():
        report = line.strip()
        if not totals:
            totals = [[0 for i in range(2)] for j in range(len(report))]
        for i,c in enumerate(report):
            totals[i][int(c)] += 1

gamma = ''
epsilon = ''
for pair in totals:
    if pair[0] > pair[1]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'


gamma = int(gamma,2)
epsilon = int(epsilon,2)
print(gamma*epsilon)
