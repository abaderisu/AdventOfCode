#!/usr/bin/env python3

from day3 import findPartNumbers

lines = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*..13
.664.598.^'''

nums,gears = findPartNumbers(lines.split('\n'))
assert nums == [467,35,633,617,592,755,13,664,598],nums
assert sum(nums) == 4374
assert sum(gears) == 467835

lines = '''.......................*......*
...910*...............233..189.
2......391.....789*............
...................983.........
0........106-...............226
.%............................$
...*......$812......812..851...
.99.711.............+.....*....
...........................113.
28*.....411....%...............'''

nums,gears = findPartNumbers(lines.split('\n'))
assert sum(nums) == 7253,nums
