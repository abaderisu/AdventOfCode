#!/usr/bin/env python3

import sys

def count_nice_strings(strings):
    nice = 0
    for string in strings:
        last = ''
        lastpair = ''
        repeat = False
        pairs = {}
        print(string)
        for c in string:
            if len(last + c) > 1 and last + c != lastpair:
                if last + c not in pairs:
                    pairs[last + c] = 1
                else:
                    pairs[last + c] += 1
            elif last + c == lastpair:
                print(last + c + ' matches ' + lastpair)
            repeat = repeat or (len(lastpair) > 1 and c == lastpair[0])
            lastpair = last + c 
            last = c
        pair = False
        for v in pairs.values():
            if v > 1:
                pair = True
                break
        if repeat and pair: 
            nice += 1
        
    return nice


if __name__ == "__main__":
    strings = [line.strip() for line in open(sys.argv[1])]
    print(count_nice_strings(strings))
