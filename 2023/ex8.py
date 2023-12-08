#!/usr/bin/python3

from math import lcm
from multiprocessing import Process, Queue

def get_resultA(loop, network, start, target, queue):
    result, step = 0, 0
    current = start
    while True:
        result += 1
        choices = network[current]
        if loop[step] == 'L':
            current = choices[1:4]
        else:
            current = choices[6:9]
        if current.endswith(target):
            if queue:
                queue.put(result)
            return result
        if step+1 == len(loop):
            step = 0
        else:
            step += 1

def get_resultB(loop, network, starts, target):
    result, processes, queue = 0, [], Queue()
    for start in sources:
        p = Process(target=get_resultA, args=(loop, network, start, target, queue))
        processes.append(p)
        p.start()
    combined_results = []
    for p in processes:
        combined_results.append(queue.get())
        p.join()
    result = lcm(*combined_results)
    return result

if __name__ == '__main__':
    with open('input/input8.txt') as input:
        network, sources = {}, []
        loop, nodes = input.read().split('\n\n')
        for node in nodes.strip().split('\n'):
            pieces = node.split(' = ')
            network[pieces[0]] = pieces[1]
            if pieces[0].endswith('A'):
                sources.append(pieces[0])
        print(get_resultA(loop, network, 'AAA', 'ZZZ', None), get_resultB(loop, network, sources, 'Z'))
