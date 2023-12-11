#!/usr/bin/python3

def distance(factor = 1):
    result = 0
    for i, g in enumerate(galaxies):
        for j, o in enumerate(galaxies):
            if o[0] > g[0] or (o[0] == g[0] and o[1] > g[1]):
                down = o[0] - g[0] + sum([factor for r in range(g[0]+1,o[0]) if r in empty_rows])
                over = max(o[1], g[1]) - min(o[1], g[1]) + sum([factor for c in range(min(g[1],o[1]), max(g[1],o[1])) if c in empty_columns])
                result += down + over
    return result

if __name__ == '__main__':
    with open('input/input11.txt') as input:
        graph = input.read().splitlines()
        empty_rows = [i for i, r in enumerate(graph) if not '#' in r]
        empty_columns = [c for c in range(len(graph[0])) if c not in set([c for r in graph for c in range(len(graph[0])) if r[c] == '#'])]
        galaxies = [(r, c) for r, d in enumerate(graph) for c in range(len(graph[0])) if d[c] == '#']
        print(distance(), distance(1000000-1))
