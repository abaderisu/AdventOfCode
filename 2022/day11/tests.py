#!/usr/bin/env python3

from day11 import monkey,playRounds
import copy

monkeys = []
monkeys.append(monkey([79,98],lambda x:x * 19,lambda x:x % 23 == 0,2,3))
monkeys.append(monkey([54,65,75,74],lambda x:x + 6,lambda x:x % 19 == 0,2, 0))
monkeys.append(monkey([79,60,97],lambda x:x*x,lambda x:x % 13 == 0,1,3))
monkeys.append(monkey([74],lambda x:x+3,lambda x:x % 17 == 0,0,1))

r1 = copy.deepcopy(monkeys)
v = playRounds(r1,20)
assert r1[0].inspected == 101
assert r1[0].items == [10,12,14,26,34],monkeys[0].items
assert r1[1].inspected == 95
assert r1[1].items == [245,93,53,199,115],monkeys[1].items
assert r1[2].inspected == 7
assert r1[2].items == []
assert r1[3].inspected == 105
assert r1[3].items == []
assert v == 10605

r2 = copy.deepcopy(monkeys)
v = playRounds(r2,10000,96577)
assert r2[0].inspected == 52166,monkeys[0].inspected
assert r2[1].inspected == 47830
assert r2[2].inspected == 1938
assert r2[3].inspected == 52013
assert v == 2713310158
