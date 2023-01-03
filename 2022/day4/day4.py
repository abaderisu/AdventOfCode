#!/usr/bin/env python3

def range_to_list(r):
    ret = []
    r = r.split('-')
    for i in range(int(r[0]),int(r[1])+1):
        ret.append(i)

    return ret

def fully_contained(l1,l2):
    return all(item in l1 for item in l2) or all(item in l2 for item in l1)

def any_contained(l1,l2):
    return any(item in l1 for item in l2) or any(item in l2 for item in l1)

if __name__ == "__main__":
    part1 = 0
    part2 = 0
    for line in open('input.txt').readlines():
        split = line.strip().split(',')

        r1 = range_to_list(split[0])    
        r2 = range_to_list(split[1])

        if fully_contained(r1,r2):
            part1 += 1
        if any_contained(r1,r2):
            part2 += 1

    print('Part 1',part1)
    print('Part 2',part2)
