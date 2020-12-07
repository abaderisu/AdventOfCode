#!/usr/bin/env python3

def escape_string(string):
    i = 0
    while i < len(string):
        c = string[i]
        if c == '"':
            i+=1
            continue
        elif c == '\\':
            n = string[i+1]
            if n == 'x':
                i+=4
                yield 'x' # the hex chars in the input aren't actually ASCII, so, lie
            else:
                i+=2
                yield n
        else:
            i+=1
            yield c

t_total = 0
t_escaped = 0
for line in open('input.txt'):
    line = line.strip()
    t_total += len(line)
    t_escaped += len(''.join([c for c in escape_string(line)]))
print(t_total - t_escaped)
