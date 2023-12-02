#!/usr/bin/python3

def priority(i):
    if ord(i) > 90:
        return ord(i)-96
    return ord(i)-38

with open('input3.txt') as input:
    a_total = 0
    b_total = 0
    group = []
    for line in input.read().splitlines():
        midpoint = int(len(line)/2)
        left = line[:midpoint]
        right = line[midpoint:]
        #print(left, right, line)
        group.append(line)
        if len(group) == 3:
            for item in group[0]:
                if item in group[1] and item in group[2]:
                    b_total += priority(item)
                    break
            group = []
        for item in left:
            if item in right:
                #print(item, 'in both', left, right, priority(item))
                a_total += priority(item)
                break
    print(a_total)
    print(b_total)

