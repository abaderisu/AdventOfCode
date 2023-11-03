#!/usr/bin/env python3

def fillTerrain(lines):
  terrain = []
  for y in range(len(lines)):
    terrain.append([0 for x in range(len(lines[0]))])
    for x in range(len(lines[0])):
      height = lines[y][x]
      if height == 'S':
        start = (x,y)
        height = 'a'
      elif height == 'E':
        end = (x,y)
        height = 'z'

      terrain[y][x] = ord(height)

  return terrain,start,end

def findNeighbors(terrain,node):
  x_min = 0
  x_max = len(terrain[0]) - 1
  y_min = 0
  y_max = len(terrain) - 1
  x, y = node

  neighbors = []
  height = terrain[y][x] - 2

  if x > x_min and terrain[y][x - 1] > height:
    neighbors.append((x - 1, y))
  if x < x_max and terrain[y][x + 1] > height:
    neighbors.append((x + 1, y))
  if y > y_min and terrain[y - 1][x] > height:
    neighbors.append((x, y - 1))
  if y < y_max and terrain[y + 1][x] > height:
    neighbors.append((x, y + 1))

  return neighbors

def walkPath(terrain,end):
  dists = {end : 0}
  path = [end]
  trails = {}
  while path:
    cur = path.pop(0)
    for n in findNeighbors(terrain,cur):
      if n not in dists:
        dists[n] = dists[cur] + 1
        path.append(n)
        if terrain[n[1]][n[0]] == ord('a'):
          trails[n] = dists[n]

  return trails

if __name__ == '__main__':
  terrain,start,end = fillTerrain(open('input.txt').readlines())
  trails = walkPath(terrain,end)
  print('Part 1', trails[start])
  print('Part 2', min([d for d in trails.values()]))

