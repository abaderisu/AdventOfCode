#!/usr/bin/env python3
from day9 import point,play

head = point()
tail = point()

head.move('D')
assert head.x == 0 and head.y == -1
head.move('U')
assert head.x == 0 and head.y == 0
head.move('R')
assert head.x == 1 and head.y == 0
head.move('L')
assert head.x == 0 and head.y == 0
assert head.visited == {(0,0),(0,-1),(1,0)}

head.move('R')
head.move('U')
tail.follow(head)
assert tail.x == 0 and tail.y == 0
head.move('R')
tail.follow(head)
assert tail.x == 1 and tail.y == 1 and tail.visited == {(0,0),(1,1)}
head.move('U')
tail.follow(head)
assert tail.x == 1 and tail.y == 1 and tail.visited == {(0,0),(1,1)}
head.move('R')
tail.follow(head)
assert tail.x == 2 and tail.y == 2 and tail.visited == {(0,0),(1,1),(2,2)},tail
head.move('L')
tail.follow(head)
assert tail.x == 2 and tail.y == 2 and tail.visited == {(0,0),(1,1),(2,2)},tail
head.move('L')
head.move('L')
tail.follow(head)
assert tail.x == 1 and tail.y == 2 and tail.visited == {(0,0),(1,1),(1,2),(2,2)},tail

moves = [['R',4],
         ['U',4],
         ['L',3],
         ['D',1],
         ['R',4],
         ['D',1],
         ['L',5],
         ['R',2]]

knots = play(moves,10)
assert knots[1].x == 1 and knots[1].y == 2 and len(knots[1].visited) == 13,knots[1]
assert knots[9].x == 0 and knots[9].y == 0 and len(knots[9].visited) == 1, knots[9]

moves = [['R',5],
         ['U',8],
         ['L',8],
         ['D',3],
         ['R',17],
         ['D',10],
         ['L',25],
         ['U',20]]
knots = play(moves,10)
assert knots[9].x == -11 and knots[9].y == 6 and len(knots[9].visited) == 36,knots[9]
