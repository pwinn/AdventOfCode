#!/usr/bin/python3

from collections import defaultdict
from functools import reduce
import operator

def get_resultA(times, distances):
    result = 0
    wins = defaultdict(int)
    for i in range(len(times)):
        for s in range(1, times[i]):
            if (times[i]-s) * s > distances[i]:
                wins[i] += 1
    result = reduce(operator.mul, wins.values(), 1)
    return result

def get_resultB(times, distances):
    wins = 0
    time = int(''.join([str(t) for t in times]))
    distance = int(''.join([str(d) for d in distances]))
    for s in range(1, time):
        if (time-s) * s > distance:
            wins += 1
    return wins

if __name__ == '__main__':
    with open('input/input6.txt') as input:
        lines = input.read().split('\n')
        times = [int(x) for x in lines[0].split(":")[1].split()]
        distances = [int(x) for x in lines[1].split(":")[1].split()]
        print(get_resultA(times, distances), get_resultB(times, distances))
