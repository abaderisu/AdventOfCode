#!/usr/bin/env python3

def parseGame(s):
    cubes = {'red':0,'blue':0,'green':0}
    id = int(s.split(':')[0][4:])
    sets = s.split(':')[1].strip().split(';')
    for set in sets:
        pulls = set.strip().split(',')
        for pull in pulls:
            num,color = pull.strip().split(' ')
            num = int(num)
            if num > cubes[color]:
                cubes[color] = num
    return id,cubes

def possible(cubes,key):
    for k,v in key.items():
        if k not in cubes:
            return False
        if v < cubes[k]:
            return False
    return True

def possibleGames(lines,key):
    ids = []
    for l in lines:
        id,cubes = parseGame(l)
        if possible(cubes,key):
            ids.append(id)
    return ids

def power(lines):
    p = 0
    for l in lines:
        _,cubes = parseGame(l)
        p = p + (cubes['red'] * cubes['green'] * cubes['blue'])
    return p

if __name__ == '__main__':
    lines = open('input.txt').readlines()
    key = {'red':12,'green':13,'blue':14}
    print('Part 1',sum(possibleGames(lines,key)))
    print('Part 2',power(lines))
