#!/usr/bin/python3

def move_9000(stacks, qty, source, dest):
    for i in range(qty):
        stacks[dest].insert(0, stacks[source].pop(0))
    return stacks

def move_9001(stacks, qty, source, dest):
    stacks[dest] = stacks[source][:qty] + stacks[dest]
    del stacks[source][:qty]
    return stacks

def stack_tops(stacks):
    tops = ''
    for stack in stacks:
        tops += stack[0]
    return tops

with open('input5.txt') as input:
    stacks = []
    stacks2 = []
    init_required = True
    for line in input.read().splitlines():
        if init_required:
            # First iteration
            init_required = False
            for i in range(int((len(line)+1)/4)):
                stacks.append([])
                stacks2.append([])
        if len(line) > 0 and line[0] == '[':
            # Stacks definition
            for crate in range(1,4*len(stacks),4):
                if line[crate] != " ":
                    stacks[int(((crate+3)/4)-1)].append(line[crate])
                    stacks2[int(((crate+3)/4)-1)].append(line[crate])
        elif len(line) > 0 and line[:4] == 'move':
            (_, qty, _, source, _, dest) = line.split()
            stacks = move_9000(stacks, int(qty), int(source)-1, int(dest)-1)
            stacks2 = move_9001(stacks2, int(qty), int(source)-1, int(dest)-1)
    print(stack_tops(stacks))
    print(stack_tops(stacks2))
