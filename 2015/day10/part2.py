#!/usr/bin/env python3

def look_and_say(seq):
    ret = ''
    cur = seq[0]
    count = 1
    for n in seq[1:] + ' ':
        if n == cur:
            count += 1
        else:
            ret = ret + str(count) + cur
            cur = n
            count = 1
    return ret

seq = '1113222113'
for _ in range(0,50):
    seq = look_and_say(seq)
print(len(seq))
