#!/usr/bin/python3

def get_resultA(network, start, target):
    result, step = 0, 0
    current = start
    while True:
        result += 1
        choices = network[current]
        if loop[step] == 'L':
            current = choices[1:4]
        else:
            current = choices[6:9]
        if current == target:
            return result
        if step+1 == len(loop):
            step = 0
        else:
            step += 1

def get_resultB(network):
    result = 0
    return result

if __name__ == '__main__':
    with open('input/input8.txt') as input:
        network = {}
        loop, nodes = input.read().split('\n\n')
        for node in nodes.strip().split('\n'):
            pieces = node.split(' = ')
            network[pieces[0]] = pieces[1]
        print(get_resultA(network, 'AAA', 'ZZZ'), get_resultB(network))
