#!/usr/bin/env python3

from parse import compile

p = compile('{first:d}-{second:d} {char}: {password}')

lines = valid = 0
for parsed in [p.parse(line.strip()) for line in open('input.txt')]:
    password = parsed['password']
    first = password[parsed['first'] - 1] == parsed['char']
    second = password[parsed['second'] - 1] == parsed['char']
    if first ^ second:
        valid+=1
   
print(valid) 
