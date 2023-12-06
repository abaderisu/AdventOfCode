#!/usr/bin/env python3

from day2 import parseGame,possibleGames,power

lines = [
'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
]

assert parseGame(lines[0]) == (1,{'blue':6,'red':4,'green':2})

key = {'red':12,'blue':14,'green':13}
assert sum(possibleGames(lines,key)) == 8

assert power(lines) == 2286
