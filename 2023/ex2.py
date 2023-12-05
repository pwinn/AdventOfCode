#!/usr/bin/python3

from functools import reduce
import operator

if __name__ == '__main__':
    with open('input/input2.txt') as input:
        maxes = {'red': 12, 'green': 13, 'blue': 14}
        resultA, resultB = 0, 0
        for line in input.read().splitlines():
            # A
            okay = True
            game, results = line.split(':')
            dice = results.replace(';',',').split(',')
            for die in dice:
                cnt, color = die.split()
                if int(cnt) > maxes[color]:
                    okay = False
                    continue
            if okay:
                resultA += int(game.split()[1])
            # B
            mins = {'red': 0, 'green': 0, 'blue': 0}
            for result in results.split(';'):
                dice = result.split(',')
                for die in dice:
                    cnt, color = die.split()
                    if int(cnt) > mins[color]:
                        mins[color] = int(cnt)
            resultB += reduce(operator.mul, mins.values(), 1)
        print(resultA, resultB)
