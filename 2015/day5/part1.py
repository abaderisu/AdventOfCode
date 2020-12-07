#!/usr/bin/env python3

import sys

nice = 0
with open(sys.argv[1]) as f:
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    bad_list = ['ab', 'cd', 'pq', 'xy']
    for line in f.readlines():
        last = ''
        double = False
        bad = False
        vowels = 0
        for c in line:
            double = double or (last == c)
            if c in vowel_list:
                vowels += 1
            bad = bad or last + c in bad_list
            last = c

        if double and (vowels >= 3) and not bad:
            nice += 1
print(nice)
