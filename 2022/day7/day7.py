#!/usr/bin/env python3

class Tree:
    def __init__(self,name,parent):
        self.children = []
        self.data = dict()
        self.name = name
        self.parent = parent

    def find(self,child_name):
        if child_name == '..':
            return self.parent
        
        if self.name == child_name:
            return self

        for c in self.children:
            if c.name == child_name:
                return c

        for c in self.children:
            found = c.find(child_name)
            if found:
                return found

    def addChild(self,name):
        self.children.append(Tree(name,self))

    def addData(self,key,value):
        self.data[key] = value

    def __iter__(self):
        yield self

        for c in self.children:
            for cc in c:
                yield cc

def parse_filesystem(commands):
    root = Tree('/',None)
    cur_dir = root

    for c in commands:
        if c.startswith('$ cd '):
            cur_dir = cur_dir.find(c[5:])
            assert cur_dir
        elif c == '$ ls':
            pass
        elif c.startswith('dir '):
            cur_dir.addChild(c[4:])
        else:
            data = c.split()
            cur_dir.addData(data[1],int(data[0]))

    return root

def total_size(tree):
    total = 0
    for n in tree:
        for v in n.data.values():
            total += v
    return total

def dir_totals_less_than(tree,max_size):
    totals = []
    for n in tree:
        total = total_size(n)
        if total < max_size:
            totals.append(total)

    return totals

def dir_totals_greater_than(tree,min_size):
    totals = []
    for n in tree:
        total = total_size(n)
        if total > min_size:
            totals.append(total)

    return totals

if __name__ == '__main__':
    fs = parse_filesystem([line.strip() for line in open('input.txt').readlines()])
    print('Part 1',sum(dir_totals_less_than(fs,100000)))
    free_space = 70000000-total_size(fs)
    to_remove = 30000000-free_space
    print('Part 2',min(dir_totals_greater_than(fs,to_remove)))
