#!/usr/bin/python3

num_elves = 3

with open('input1.txt') as input:
    elf = []
    calories = 0
    for line in input.read().splitlines():
        if len(line) < 1:
            elf.append(calories)
            calories = 0
            continue
        calories += int(line)
    if calories > 0:
        elf.append(calories)
    elf.sort()
    print(sum(elf[-num_elves:]))


