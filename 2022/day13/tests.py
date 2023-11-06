#!/usr/bin/env python3

from day13 import orderedPairs,findDecoderKey

lines='''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''

total,packets = orderedPairs(lines.split('\n'))
assert total == 13,total
key = findDecoderKey(packets)
assert key == 140,key
