#!/usr/bin/env python3

import copy
import re

def parse_puzzle(puzzle):
    parsed = None    
    for line in puzzle:
        m = re.findall('\[(\w)\]\s|\s\s\s\s',line)
        if parsed is None:
            parsed = [[] for _ in  range(len(m))]
        for i in range(len(m)):
            if m[i] != '':
                parsed[i].insert(0,m[i])

    return parsed


def puzzle_move(move,puzzle):
    parsed = re.fullmatch('move (\d+) from (\d+) to (\d+)', move).groups()
    for _ in range(int(parsed[0])):
        puzzle[int(parsed[2])-1].append(puzzle[int(parsed[1])-1].pop())

def puzzle_move2(move,puzzle):
    parsed = re.fullmatch('move (\d+) from (\d+) to (\d+)', move).groups()
    temp = []
    s1 = int(parsed[1])-1
    s2 = int(parsed[2])-1
    for _ in range(int(parsed[0])):
        temp.insert(0,puzzle[s1].pop())
    puzzle[s2].extend(temp)

if __name__ == '__main__':
    puzzle = []
    moves = []
    for line in open('input.txt').readlines():
        if '[' in line:
            puzzle.append(line)
        elif line.startswith('move'):
            moves.append(line.strip())

    puzzle = parse_puzzle(puzzle)
    puzzle2 = copy.deepcopy(puzzle)
    for move in moves:
        puzzle_move(move,puzzle)
        puzzle_move2(move,puzzle2)

    part1=''.join([stack[-1] for stack in puzzle])
    print('Part 1',part1)

    part2=''.join([stack[-1] for stack in puzzle2])
    print('Part 2',part2)
