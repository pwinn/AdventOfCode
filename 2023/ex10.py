#!/usr/bin/python3

import re

def north(graph, row, column):
    return graph[row-1][column] if row > 0 else None

def east(graph, row, column):
    return graph[row][column+1] if len(graph[row]) >= column else None

def south(graph, row, column):
    return graph[row+1][column] if len(graph) >= row else None

def west(graph, row, column):
    return graph[row][column-1] if column > 0 else None

def get_loop(graph, row, col):
    last, loop = None, []
    while last is None or graph[row][col] != 'S':
        current = graph[row][col]
        if last != 'south' and current in ['S', '|', 'L', 'J'] and north(graph, row, col) in ['|', '7', 'F', 'S']:
            row -= 1
            last = 'north'
        elif last != 'west' and current in ['S', '-', 'L', 'F'] and east(graph, row, col) in ['-', 'J', '7', 'S']:
            col += 1
            last = 'east'
        elif last != 'north' and current in ['S', '|', '7', 'F'] and south(graph, row, col) in ['|', 'L', 'J', 'S']:
            row += 1
            last = 'south'
        elif last != 'east' and current in ['S', '-', '7', 'J'] and west(graph, row, col) in ['-', 'L', 'F', 'S']:
            col -= 1
            last = 'west'
        else:
            print('shit')
        loop.append((row, col))
    return loop

def determine_start(graph, row, col):
    # Could be anything, hard-coding for now
    return 'J'

def result_a(graph, row, col):
    return len(get_loop(graph, row, col)) // 2

def result_b(graph, row, col):
    result = 0
    # Do the loop again, but this time store each coordinate set
    loop = get_loop(graph, row, col)
    graph[row][col] = determine_start(graph, row, col)
    # Anything non-loop is a .
    for row in range(len(graph)):
        for col in range(len(graph[row])):
            if (row, col) not in loop:
                graph[row][col] = '.'
    # Replace L7 and FJ combos with |
    for line_num, line in enumerate(graph):
        line = list(re.sub('L-*7', '|', ''.join(line)))
        line = list(re.sub('F-*J', '|', ''.join(line)))
        graph[line_num] = line
    # For each non-loop, count the | to their left. 0 or Odd = out, Even = in
        pipes = 0
        for ch in line:
            #print(ch, pipes, pipes % 2, result)
            if ch == '|':
                pipes += 1
            if ch == '.' and pipes % 2 > 0:
                result += 1
    #for row in range(len(graph)):
    #    for col in range(len(graph[row])):
    #        if graph[row][col] == '.':
    #            print(graph[row][:col], graph[row][:col].count('|'), 'mod', graph[row][:col].count('|') % 2)
    #            if graph[row][:col].count('|') % 2:
    #                result += 1
    #                graph[row][col] = '*'
    #            #print('mod', graph[row][:col].count('|') % 2, 'result', result)
    #        if col == len(graph[row])-1:
    #            print(''.join(graph[row]))
    return result
    

if __name__ == '__main__':
    with open('input/input10.txt') as input:
        graph = []
        for row, line in enumerate(input.read().splitlines()):
            if 'S' in line:
                start_row, start_col = row, line.index('S')
            graph.append(list(line))
        print(result_a(graph, start_row, start_col), result_b(graph, start_row, start_col))
