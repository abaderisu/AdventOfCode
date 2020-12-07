#!/usr/bin/env python3

from parse import compile

outer = compile('{bag} bags contain {contents}')
inner = compile('{amount:d} {bag} bag')

def can_contain(target, bag, rules):
    children = rules[bag]

    if target in children:
        return True

    for child in children:
        if can_contain(target, child, rules):
            return True

    return False

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
        bag_rules[bag].append(parsed['bag'])

print(len([bag for bag in bag_rules if can_contain('shiny gold', bag, bag_rules) is True]))
