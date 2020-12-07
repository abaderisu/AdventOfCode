#!/usr/bin/env python3

def encode_string(string):
    yield '"'
    for i in range(0,len(string)):
        c = string[i]
        if c == '"':
            yield '\\'
        elif c == '\\':
            yield '\\'
        yield c
    yield '"'

t_total = 0
t_encoded = 0
for line in open('input.txt'):
    line = line.strip()
    t_total += len(line)
    t_encoded += len(''.join([c for c in encode_string(line)]))
print(t_encoded - t_total)
