#!/usr/bin/python3

from functools import reduce

def trace_seed(seed):
    for i in range(len(maps)):
      for m in maps[i]:
        if len(m) > 0 and m[1] <= seed <= (m[1] + m[2]):
            seed += m[0] - m[1]
            break
    return seed

def get_resultA(seeds):
    result = []
    mapped_seeds = []
    for seed in seeds:
        mapped_seeds.append(trace_seed(seed))
    return min(mapped_seeds)

def get_resultB(seeds):
    '''Printing each new low seed means I can submit the accepted answer without waiting for completion'''
    result = 0
    lowest_seed = None
    for i in range(0, len(seeds)-1, 2):
        for seed in range(seeds[i], seeds[i]+seeds[i+1]):
            candidate = trace_seed(seed)
            if lowest_seed is None or candidate < lowest_seed:
                lowest_seed = candidate
                print('new lowest seed', lowest_seed)
    return lowest_seed

if __name__ == '__main__':
    with open('input/input5.txt') as input:
        sections = input.read().split('\n\n')
        seeds = [int(x) for x in sections[0].split(":")[1].split()]
        maps = []
        for i in range(1, len(sections)):
            maps.append([[int(x) for x in m.split()] for m in sections[i].split("\n")[1:]])
        print(get_resultA(seeds), get_resultB(seeds))
