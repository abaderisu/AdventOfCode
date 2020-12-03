#!/usr/bin/env python3

from parse import compile

p = compile('{min:d}-{max:d} {char}: {password}')

valid = 0
for parsed in [p.parse(line.strip()) for line in open('input.txt')]:
    c = parsed['password'].count(parsed['char'])
    if c >= parsed['min'] and c <= parsed['max']:
        valid+=1
   
print(valid) 
