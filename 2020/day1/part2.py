#!/usr/bin/env python3

import sys

values = []
with open(sys.argv[1]) as f:
    for line in f.readlines():
        values.append( int(line.strip()) )

values.sort()
product = 0
for i in range(0, len(values)):
    for j in range(i + 1, len(values)):
        for k in range(len(values) - 1, j, -1):
            if values[i] + values[j] + values[k] == 2020:
                product = values[i] * values[j] * values[k]
                break
        if product != 0:
            break

    if product != 0:
        break

print(product)
