#!/usr/bin/env python3

from day8 import parse_tree,num_visible,is_visible,scenic_score,highest_score

input = [
    '30373',
    '25512',
    '65332',
    '33549',
    '35390'
]

tree = parse_tree(input)
assert is_visible(1,1,tree) is True
assert is_visible(1,2,tree) is True
assert is_visible(1,3,tree) is False
assert is_visible(2,1,tree) is True
assert is_visible(2,2,tree) is False
assert is_visible(2,3,tree) is True
assert is_visible(3,1,tree) is False
assert is_visible(3,2,tree) is True
assert is_visible(3,3,tree) is False
assert num_visible(tree) == 21

assert scenic_score(1,2,tree) == 4
assert scenic_score(3,2,tree) == 8
assert highest_score(tree) == 8
