#!/usr/bin/env python3

from day11 import monkey,playRounds,parseMonkeys
import copy

lines = '''
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''

monkeys,lcm = parseMonkeys(lines.split('\n'))
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
v = playRounds(r2,10000,lcm)
assert r2[0].inspected == 52166,monkeys[0].inspected
assert r2[1].inspected == 47830
assert r2[2].inspected == 1938
assert r2[3].inspected == 52013
assert v == 2713310158
