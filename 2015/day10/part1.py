#!/usr/bin/env python3

def look_and_say(seq):
    ret = ''
    i = 0
    while i < len(seq):
        c = seq[i]
        j = 1
        while i + j < len(seq):
            if seq[i + j] == c:
                j += 1
            else:
                break
        ret = ret + str(j) + c
        i += j
    return ret

seq = '1113222113'
for _ in range(0,40):
    seq = look_and_say(seq)
print(len(seq))
