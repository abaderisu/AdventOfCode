#!/usr/bin/env python3

from parse import compile

p = compile('{start} to {end} = {weight:d}')

class path:
    def __init__(self, end, weight):
        self.end = end
        self.weight = weight

    def __str__(self):
        return self.end + ' ' + str(self.weight)

    def __repr__(self):
        return str(self)

    def __lt__(self, rhs):
        return self.weight <  rhs.weight

graph = {}
for line in open('input.txt'):
    parsed = p.parse(line)
    start = parsed['start']
    end = parsed['end']
    if start not in graph:
        graph[start] = []
    if end not in graph:
        graph[end] = []
    graph[start].append( path(end, parsed['weight']) )
    graph[end].append( path( start, parsed['weight'] ) )

for city in graph:
    graph[city].sort()

route = None
for city in graph:
    visited = [city]
    cost = 0
    node = city
    while len(visited) < len(graph):
        for path in graph[node]:
            if path.end not in visited:
                cost += path.weight
                visited.append(path.end)
                node = path.end
                break

    if route is None or cost < route:
        route = cost

print(route)    
