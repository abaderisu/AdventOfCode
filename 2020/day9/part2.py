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

def find_sequence(target, inputs):
    sequence = []
    i = 0
    while(sum(sequence) < target) and i < len(inputs):
        sequence.append(inputs[i])
        i += 1

    return sequence

inputs = [int(line.strip()) for line in open('input.txt')]
error = find_error(inputs)
for i in range(0, len(inputs)):
    sequence = find_sequence(error, inputs[i:])
    if sum(sequence) == error:
        sequence.sort()
        print(sequence[0] + sequence[len(sequence) -1])
        break
