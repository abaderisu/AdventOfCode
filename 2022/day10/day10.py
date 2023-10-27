#!/usr/bin/env python3

def draw_crt(crt, x, y, sprite):
  if x in [sprite - 1, sprite, sprite + 1]:
    crt[y][x] = '#'
  x = x + 1
  if x == 40:
    x = 0
    y = y + 1
    if y == 6:
      y = 0
 
  return crt, x, y

def execute(ops):
  vals = [1]
  cycle = 0
  x = 0
  y = 0
  crt = [['.' for _ in range(40)] for _ in range(6)]

  for op in ops:
    crt,x,y = draw_crt(crt,x,y,vals[cycle])
    vals.append(vals[cycle])
      
    cycle = cycle + 1
    if op[0] == 'addx':
      crt,x,y = draw_crt(crt,x,y,vals[cycle])
      vals.append(vals[cycle] + int(op[1]))
      cycle = cycle + 1

  return (vals,crt)

if __name__ == '__main__':
  ops = [line.split() for line in open('input.txt').readlines()]
  vals,crt = execute(ops)
  strengths = [19,59,99,139,179,219]
  p1 = sum([vals[s] * (s+1) for s in strengths])
  print(f'Part 1 {p1}')
  for row in crt:
    print(''.join(row))
