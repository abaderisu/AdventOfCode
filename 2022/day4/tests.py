#!/usr/bin/env python3

from day4 import fully_contained, range_to_list, any_contained

assert range_to_list('2-4') == [2,3,4]
assert range_to_list('6-6') == [6]

assert fully_contained(range_to_list('2-4'),range_to_list('6-8')) is False
assert fully_contained(range_to_list('2-3'),range_to_list('4-5')) is False
assert fully_contained(range_to_list('5-7'),range_to_list('7-9')) is False
assert fully_contained(range_to_list('2-8'),range_to_list('3-7')) is True
assert fully_contained(range_to_list('6-6'),range_to_list('4-6')) is True
assert fully_contained(range_to_list('2-6'),range_to_list('4-8')) is False

assert any_contained(range_to_list('5-7'),range_to_list('7-9')) is True
assert any_contained(range_to_list('2-8'),range_to_list('3-7')) is True
assert any_contained(range_to_list('6-6'),range_to_list('4-6')) is True
assert any_contained(range_to_list('2-6'),range_to_list('4-8')) is True
