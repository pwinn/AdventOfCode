#!/usr/bin/python3

import re

gears = {}

def symbol_is_adjacent(val, val_x, val_y):
    global gears
    for y in range(val_y-1, val_y+2):
        for x in range(val_x-1, val_x+len(val)+1):
            if 0 <= y <= len(schematic)-1 and 0 <= x <= len(schematic[val_y])-1:
                if schematic[y][x] not in '1234567890.':
                    if schematic[y][x] == '*':
                        gears[(y, x)].append(val)
                    return True
    return False


if __name__ == '__main__':
    with open('input3.txt') as input:
        resultA, resultB = 0, 0
        schematic = []
        for line in input.read().splitlines():
            schematic.append(line)
        for row_num, row in enumerate(schematic):
            for col_num, char in enumerate(row):
                if char == '*':
                    gears[(row_num, col_num)] = []
        for row_num, row in enumerate(schematic):
            for match in re.finditer('\d+', row):
                if symbol_is_adjacent(match.group(0), match.start(), row_num):
                    resultA += int(match.group(0))
        for gear, vals in gears.items():
            if len(vals) > 1:
                resultB += (int(vals[0]) * int(vals[1]))
        print(resultA, resultB)
