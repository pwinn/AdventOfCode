#!/usr/bin/python3

numbers = {'zero': '0o', 'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': '4', 'five': '5e', 'six': '6', 'seven': '7n', 'eight': 'e8t', 'nine': 'n9e'}
resultA = 0
resultB = 0
with open('input1.txt') as input:
    for line in input.read().splitlines():
        # A
        digits = list(map(int, filter(str.isdigit, line)))
        resultA += (digits[0]*10) + digits[-1]
        # B (third attempt)
        lineB = line
        [lineB := lineB.replace(num, digit) for num, digit in numbers.items()]
        digitsB = list(map(int, filter(str.isdigit, lineB)))
        resultB += (digitsB[0]*10) + digitsB[-1]
    print(resultA, resultB)
