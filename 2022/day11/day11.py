#!/usr/bin/env python3

import copy

class monkey:
  def __init__(self,items,item_op,item_test,monkey_true,monkey_false):
    self.items = items
    self.item_op = item_op
    self.item_test = item_test
    self.monkey_true = monkey_true
    self.monkey_false = monkey_false
    self.inspected = 0

  def takeTurn(self,modulo):
    throws = []
    for item in self.items:
      item = self.item_op(item)
      if modulo is None:
        item = item // 3
      else:
        item = item % modulo
      self.inspected = self.inspected + 1

      throw_to = self.monkey_false 
      if self.item_test(item):
        throw_to = self.monkey_true

      throws.append((throw_to, item))
    
    self.items.clear()
    return throws

def playRound(monkeys,modulo=None):
  for m in monkeys:
    throws = m.takeTurn(modulo)
    for t in throws:
      monkeys[t[0]].items.append(t[1])

  return monkeys

def playRounds(monkeys,count,modulo=None):
  for _ in range(count):
    playRound(monkeys,modulo)

  h1 = max([m.inspected for m in monkeys])
  h2 = max([m.inspected for m in monkeys if m.inspected < h1])
  return h1 * h2

if __name__=='__main__':
  monkeys = []
  lines = open('input.txt').readlines()
  modulo = 1
  for i in range(len(lines)):
    if lines[i].startswith('Monkey'):
      i = i + 1
      items = [int(i) for i in lines[i][17:].split(',')]
      i = i + 1
      line = lines[i][lines[i].index('=') + 1:].strip().split()
      if line[1] == '+':
        item_op = lambda x, arg=int(line[2]):x + arg
      elif line[1] == '*':
        if line[2] == 'old':
          item_op = lambda x:x * x
        else:
          item_op = lambda x, arg=int(line[2]):x * arg
      i = i + 1
      line = lines[i][lines[i].index('by') + 2:]
      modulo = modulo * int(line)
      item_test = lambda x, arg=int(line): x % arg == 0
      i = i + 1
      monkey_true = int(lines[i][lines[i].index('monkey') + 6:])
      i = i + 1
      monkey_false = int(lines[i][lines[i].index('monkey') + 6:])

      monkeys.append(monkey(items,item_op,item_test,monkey_true,monkey_false))

  p1 = copy.deepcopy(monkeys)
  print(playRounds(p1,20))

  p2 = copy.deepcopy(monkeys)
  print(playRounds(p2,10000,modulo))
