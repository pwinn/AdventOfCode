#!/usr/bin/python3

with open('input6.txt') as input:
    data = input.read()
    match4 = 0
    for i in range(len(data)):
        if match4 == 0 and len(set(data[i:i+4])) == 4:
            match4 = i+4
        if len(set(data[i:i+14])) == 14:
            break
    print(match4)
    print(i+14)
