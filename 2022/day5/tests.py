#!/usr/bin/env python3

from day5 import parse_puzzle, puzzle_move,puzzle_move2


input=['    [D]     ','[N] [C]     ','[Z] [M] [P] ']
puzzle=parse_puzzle(input)
assert puzzle == [['Z','N'],['M','C','D'],['P']]

puzzle_move('move 1 from 2 to 1', puzzle)
assert puzzle == [['Z','N','D'],['M','C'],['P']]

puzzle_move('move 3 from 1 to 3',puzzle)
assert puzzle == [[],['M','C'],['P','D','N','Z']]

puzzle_move('move 2 from 2 to 1',puzzle)
assert puzzle == [['C','M'],[],['P','D','N','Z']]

puzzle_move('move 1 from 1 to 2',puzzle)
assert puzzle == [['C'],['M'],['P','D','N','Z']]

puzzle2=parse_puzzle(input)
puzzle_move2('move 1 from 2 to 1',puzzle2)
assert puzzle2 == [['Z','N','D'],['M','C'],['P']]

puzzle_move2('move 3 from 1 to 3',puzzle2)
assert puzzle2 == [[],['M','C'],['P','Z','N','D']]

puzzle_move2('move 2 from 2 to 1',puzzle2)
assert puzzle2 == [['M','C'],[],['P','Z','N','D']]

puzzle_move2('move 1 from 1 to 2',puzzle2)
assert puzzle2 == [['M'],['C'],['P','Z','N','D']]
