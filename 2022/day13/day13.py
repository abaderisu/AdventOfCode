#!/usr/bin/env python3

def partition(packets,start,end):
  pivot = packets[end]
  index = start - 1

  for i in range(start,end):
    if ordered(packets[i],pivot):
      index = index + 1

      temp = packets[index]
      packets[index] = packets[i]
      packets[i] = temp

  temp = packets[index + 1]
  packets[index + 1] = packets[end]
  packets[end] = temp

  return index + 1

def quicksort(packets,start,end):
  if start < end:
    pivot = partition(packets,start,end)
    quicksort(packets, start, pivot - 1)
    quicksort(packets, pivot + 1, end)

def ordered(left,right):
  if type(left) is int:
    if type(right) is int:
      return None if left == right else left < right
    else:
      return ordered([left],right)
  else:
    if type(right) is int:
      right = [right]

    for i in range(len(left)):
      if i == len(right):
        return False
      order = ordered(left[i],right[i])
      if order is not None:
        return order

    if len(left) < len(right):
      return True

  return None

def orderedPairs(lines):
  left = None
  right = None
  pairs = 1
  total = 0
  packets = []
  for line in lines:
    if len(line.strip()) == 0:
      continue

    if left is None:
      left = eval(line)
    else:
      right = eval(line)
      order = ordered(left,right)
      if order is None:
        raise RuntimeException(f'Pair {pairs} resulted in none')
      if order:
        total = total + pairs

      pairs = pairs + 1
      packets.append(left)
      packets.append(right)
      left = None
      right = None
  return total,packets

def findDecoderKey(packets):
  k1 = [[2]]
  k2 = [[6]]
  packets.append(k1)
  packets.append(k2)

  quicksort(packets,0,len(packets) - 1)
  return (packets.index(k1) + 1) * (packets.index(k2) + 1)

if __name__ == '__main__':
  lines = open('input.txt').readlines()
  total,packets = orderedPairs(lines)
  print(f'Part 1 {total}')
  print(f'Part 2 {findDecoderKey(packets)}')
