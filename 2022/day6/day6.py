#!/usr/bin/env python3

def first_non_repeating(sequence,length):
    for i in range(length-1,len(sequence)):
        if len(set(sequence[i-length+1:i+1])) == length:
            return i+1

def find_packet(sequence):
    return first_non_repeating(sequence,4)

def find_message(sequence):
    return first_non_repeating(sequence,14)

if __name__ == '__main__':
    sequence = open('input.txt').read().strip()
    print(find_packet(sequence))
    print(find_message(sequence))
