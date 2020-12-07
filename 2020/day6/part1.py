#!/usr/bin/env python3

lines = [line.strip() for line in open('input.txt')]
def splitter(lines):
    group = ''
    for line in lines:
        if line == '':
            yield group
            group = ''
        else:
            group = group + line
print(sum([len(set(group)) for group in splitter(lines)]))
