#!/usr/bin/python3

import math
from multiprocessing import Process, Queue

def count_steps(loop, network, start, target, queue=None):
    step, current = 0, start
    while not current.endswith(target):
        if loop[step%len(loop)] == 'L':
            current = network[current][1:4]
        else:
            current = network[current][6:9]
        step += 1
    if queue:
        queue.put(step)
    return step

def get_resultB(starts, target):
    processes, queue = [], Queue()
    # Count in parallel
    for start in sources:
        p = Process(target=count_steps, args=(loop, network, start, target, queue))
        processes.append(p)
        p.start()
    # Collect parallel results
    combined_results = []
    for p in processes:
        combined_results.append(queue.get())
        p.join()
    # Math is nice
    return math.lcm(*combined_results)

if __name__ == '__main__':
    with open('input/input8.txt') as input:
        network, sources = {}, []
        loop, nodes = input.read().strip().split('\n\n')
        for node in nodes.split('\n'):
            pieces = node.split(' = ')
            network[pieces[0]] = pieces[1]
            if pieces[0].endswith('A'):
                sources.append(pieces[0])
        print(count_steps(loop, network, 'AAA', 'ZZZ'), get_resultB(sources, 'Z'))
