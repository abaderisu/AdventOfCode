#!/usr/bin/env python3

import sys

values = []
with open(sys.argv[1]) as f:
    for line in f.readlines():
        values.append( int(line.strip()) )

values.sort()
product = 0
for i in range(0, len(values)):
    for j in range(len(values) - 1, i, -1):
        if values[i] + values[j] == 2020:
            product = values[i] * values[j]
            break

    if product != 0:
        break

print(product)
