#!/usr/bin/env python3

from parse import compile

p = compile('{source} -> {sink}')

signals = {'b':956}

def find_source(source, instructions):
    sig = signals.get(source)
    if sig is None:
        sig = signal(source, instructions)
        signals[source] = sig
    return sig

def signal(sink, instructions):
    if sink.isnumeric():
        return int(sink)

    source = instructions[sink].split( ' ' )
    if len(source) == 1:
        sig = find_source(source[0], instructions)
        return sig
    elif len(source) == 2:
        sig = ~find_source(source[1], instructions)
        return sig
    elif len(source) == 3:
        if source[1] == 'AND':
            s1 = find_source(source[0], instructions)
            s2 = find_source(source[2], instructions)
            return s1 & s2

        elif source[1] == 'OR':
            s1 = find_source(source[0], instructions)
            s2 = find_source(source[2], instructions)
            return s1 | s2

        elif source[1] == 'RSHIFT':
            s1 = find_source(source[0], instructions)
            return s1 >> int(source[2])

        elif source[1] == 'LSHIFT':
            s1 = find_source(source[0], instructions)
            return s1 << int(source[2])

    print('Bad sink ' + sink )
    return 0

instructions = {}
for instruction in [p.parse(line.strip()) for line in open('input.txt')]:
    instructions[instruction['sink']] = instruction['source']

print(signal('a', instructions))
