#!/usr/bin/python3

with open('input4.txt') as input:
    a_count = 0
    b_count = 0
    for line in input.read().splitlines():
        (left, right) = line.split(',')
        (left_start, left_end) = left.split('-')
        (right_start, right_end) = right.split('-')
        if int(left_start) <= int(right_start) and int(left_end) >= int(right_end):
            a_count += 1
        elif int(left_start) >= int(right_start) and int(left_end) <= int(right_end):
            a_count += 1
        if int(left_start) <= int(right_end) and int(left_end) >= int(right_start):
            b_count += 1
    print(a_count)
    print(b_count)
