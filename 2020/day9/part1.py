#!/usr/bin/env python3

def is_sum(preamble, i):
    for p in preamble:
        if abs(i - p) in preamble:
            return True
    return False

def find_error(inputs):
    preamble = []
    for i,v in enumerate(inputs):
        if len(preamble) < 25:
            preamble.append(v)
        else:
            if is_sum(preamble, v):
                preamble.pop(0)
                preamble.append(v)
            else:
                return v
    return -1

inputs = [int(line.strip()) for line in open('input.txt')]
print(find_error(inputs))
