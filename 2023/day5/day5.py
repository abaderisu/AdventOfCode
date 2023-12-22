#!/usr/bin/env python3

def parse(lines):
    i = 0
    seeds = []
    mappings = []

    while i < len(lines):
        if lines[i].startswith('seeds:'):
            seeds = [int(s) for s in lines[i].split('seeds: ')[1].split(' ')]
        elif lines[i].endswith(':'):
            i += 1
            mapping = []
            while i < len(lines) and lines[i] != '':
                mapping.append([int(x) for x  in lines[i].split(' ')])
                i += 1
            mappings.append(mapping)

        i += 1

    p1ranges = [(s,1) for s in seeds]
    p2ranges = [(s1,s2) for s1,s2 in zip(seeds[::2], seeds[1::2])]
    return p1ranges,p2ranges,mappings

def applyMapping(mapping,ranges):
    mapped = []
    for (dest,src,length) in mapping:
        srcEnd = src + length
        leftovers = []
        while ranges:
            start,end = ranges.pop()
            left = (start,min(end,src))
            overlap = (max(start,src), min(srcEnd,end))
            right = (max(srcEnd, start), end)
            if left[1] > left[0]:
                leftovers.append(left)
            if overlap[1] > overlap[0]:
                mapped.append((overlap[0]-src+dest, overlap[1]-src+dest))
            if right[1] > right[0]:
                leftovers.append(right)
        ranges = leftovers
    return mapped + ranges

def findMinSeedLocation(seedRanges,mappings):
    mapped = []
    for sR in seedRanges:
        rangeList = [(sR[0],sR[0]+sR[1])]
        for m in mappings:
            rangeList = applyMapping(m, rangeList)
        mapped.append(min(rangeList)[0])

    return min(mapped)

if __name__ == '__main__':
    p1ranges,p2ranges,mappings = parse(open('input.txt').read().splitlines())
    print('Part 1',findMinSeedLocation(p1ranges, mappings))
    print('Part 2',findMinSeedLocation(p2ranges, mappings))
