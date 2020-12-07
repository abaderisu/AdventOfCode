#!/usr/bin/env python3

from parse import compile

outer = compile('{bag} bags contain {contents}')
inner = compile('{amount:d} {bag} bag')

def total_bags_contained(bag, rules):
    total = 0
    for child in rules[bag]:
        total += total_bags_contained(child[0], rules) * child[1] + child[1]
    return total

bag_rules = {}
for line in open('input.txt'):
    first = outer.parse(line.strip())
    bag = first['bag']
    bag_rules[bag] = []
    for content in first['contents'].split(','):
        content = content.replace('bags','bag').replace('.','').strip()
        parsed = inner.parse(content)
        if parsed is None:
            continue
        bag_rules[bag].append((parsed['bag'], parsed['amount']))
print(total_bags_contained('shiny gold', bag_rules))
