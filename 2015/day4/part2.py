#!/usr/bin/env python3

import hashlib

key = 'ckczppom'
dec = 0
while True:
    hash = hashlib.md5((key + str(dec)).encode('utf-8')).hexdigest()
    if ( hash.startswith('000000') ):
        break
    dec += 1
print(dec)
