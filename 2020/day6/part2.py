#!/usr/bin/env python3

lines = [line.strip() for line in open('input.txt')]
def splitter(lines):
    group = None
    for line in lines:
        if line == '':
            yield group
            group = None
        elif group is None:
            group = set(line)
        else:
            group = group.intersection(set(line))

print(sum([len(group) for group in splitter(lines)]))
