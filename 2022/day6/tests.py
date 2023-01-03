#!/usr/bin/env python3

from day6 import find_packet, find_message

assert find_packet('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
assert find_packet('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
assert find_packet('nppdvjthqldpwncqszvftbrmjlhg') == 6
assert find_packet('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
assert find_packet('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

assert find_message('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
assert find_message('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
assert find_message('nppdvjthqldpwncqszvftbrmjlhg') == 23
assert find_message('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
assert find_message('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26
