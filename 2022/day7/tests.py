#!/usr/bin/env python3

from day7 import parse_filesystem, total_size, dir_totals_less_than,dir_totals_greater_than

commands = [
    '$ cd /',
    '$ ls',
    'dir a',
    '14848514 b.txt',
    '8504156 c.dat',
    'dir d',
    '$ cd a',
    '$ ls',
    'dir e',
    '29116 f',
    '2557 g',
    '62596 h.lst',
    '$ cd e',
    '$ ls',
    '584 i',
    '$ cd ..',
    '$ cd ..',
    '$ cd d',
    '$ ls',
    '4060174 j',
    '8033020 d.log',
    '5626152 d.ext',
    '7214296 k'
]
fs = parse_filesystem(commands)
assert total_size(fs.find('e')) == 584
assert total_size(fs.find('a')) == 94853
assert total_size(fs.find('d')) == 24933642
assert total_size(fs.find('/')) == 48381165
assert sum(dir_totals_less_than(fs,100000)) == 95437
assert min(dir_totals_greater_than(fs,8381165)) == 24933642
