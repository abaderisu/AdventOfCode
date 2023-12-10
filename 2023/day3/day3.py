#!/usr/bin/env python3

def validNeighbors(x,y,grid):
    neighbors = []
    if x > 0:
        neighbors.append((x-1,y))
        if y > 0:
            neighbors.append((x-1,y-1))
        if y < len(grid) - 1:
            neighbors.append((x-1,y+1))
    if x < len(grid[y]) - 1:
        neighbors.append((x+1,y))
        if y > 0:
            neighbors.append((x+1,y-1))
        if y < len(grid) - 1:
            neighbors.append((x+1,y+1))
    if y > 0:
        neighbors.append((x,y-1))
    if y < len(grid) - 1:
        neighbors.append((x,y+1))

    return neighbors

def findPartNumbers(grid):
    partNumbers = []
    gears = dict()
    for y in range(len(grid)):
        num = ''
        foundSymbol = False
        gearNeighbors = set()
        for x in range(len(grid[y])):
            if grid[y][x].isdigit():
                num = num + grid[y][x]
                for n in validNeighbors(x,y,grid):
                    if grid[n[1]][n[0]] != '.' and not grid[n[1]][n[0]].isdigit():
                        foundSymbol = True
                        if grid[n[1]][n[0]] == '*':
                            gearNeighbors.add(n)
            else:
                if foundSymbol:
                    partNumbers.append(int(num))
                    for gn in gearNeighbors:
                        v = (1,0)
                        if gn in gears:
                            v = gears[gn]
                        gears[gn] = (int(num) * v[0],v[1] + 1)
                num = ''
                foundSymbol = False
                gearNeighbors = set()
        if foundSymbol:
            partNumbers.append(int(num))
            for gn in gearNeighbors:
                v = (1,0)
                if gn in gears:
                    v = gears[gn]
                gears[gn] = (int(num) * v[0],v[1] + 1)

    gearRatios = [v[0] for v in gears.values() if v[1] == 2]

    return partNumbers,gearRatios

if __name__ == '__main__':
    lines = open('input.txt').read().splitlines()
    nums,gears = findPartNumbers(lines)
    print('Part 1',len(nums),sum(nums))
    print('Part 2',len(gears),sum(gears))
