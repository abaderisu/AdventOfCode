#!/usr/bin/env python3
class point:

  def __init__(self):
    self.x = 0
    self.y = 0
    self.visited = {(self.x,self.y)}

  def move(self, dir):
    if dir == 'U':
     self.y = self.y + 1
    elif dir == 'D':
     self.y = self.y - 1
    elif dir == 'L':
     self.x = self.x - 1
    elif dir == 'R':
     self.x = self.x + 1
    self.visited.add((self.x,self.y))

  def follow(self, p):
    dx = p.x - self.x
    dy = p.y - self.y
    if dx > 1:
      self.x = self.x + 1
      if dy > 0:
        self.y = self.y + 1
      elif dy < 0:
        self.y = self.y - 1
    elif dx < -1:
      self.x = self.x - 1
      if dy > 0:
        self.y = self.y + 1
      elif dy < 0:
        self.y = self.y - 1
    elif dy > 1:
      self.y = self.y + 1
      if dx > 0:
        self.x = self.x + 1
      elif dx < 0:
        self.x = self.x - 1
    elif dy < -1:
      self.y = self.y - 1
      if dx > 0:
        self.x = self.x + 1
      elif dx < 0:
        self.x = self.x - 1

    self.visited.add((self.x, self.y))

  def __str__(self):
    return f'{self.x} {self.y} {len(self.visited)}'

def play(moves,num_knots):
  knots = [point() for i in range(num_knots)]
  for m in moves:
    for i in range(m[1]):
      knots[0].move(m[0])
      for i in range(1,len(knots)):
        knots[i].follow(knots[i-1])
    print(f'{m} {knots[9]}')

  return knots

if __name__ == '__main__':
  moves = []
  for line in open('input.txt').readlines():
    line = line.split()
    moves.append([line[0],int(line[1])])

  knots = play(moves,10)
  print(f'Part 1 {len(knots[1].visited)}')
  print(f'Part 2 {len(knots[9].visited)}')
