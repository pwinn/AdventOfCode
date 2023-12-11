#!/usr/bin/python3

def north(graph, row, column):
    return graph[row-1][column] if row > 0 else None

def east(graph, row, column):
    return graph[row][column+1] if len(graph[row]) >= column else None

def south(graph, row, column):
    return graph[row+1][column] if len(graph) >= row else None

def west(graph, row, column):
    return graph[row][column-1] if column > 0 else None

def get_loop(graph, row, col):
    first, last, loop = None, None, []
    while last is None or graph[row][col] != 'S':
        current = graph[row][col]
        if last != 'south' and current in ['S', '|', 'L', 'J'] and north(graph, row, col) in ['|', '7', 'F', 'S']:
            row -= 1
            last = 'north'
            if not first:
                first = last
        elif last != 'west' and current in ['S', '-', 'L', 'F'] and east(graph, row, col) in ['-', 'J', '7', 'S']:
            col += 1
            last = 'east'
            if not first:
                first = last
        elif last != 'north' and current in ['S', '|', '7', 'F'] and south(graph, row, col) in ['|', 'L', 'J', 'S']:
            row += 1
            last = 'south'
            if not first:
                first = last
        elif last != 'east' and current in ['S', '-', '7', 'J'] and west(graph, row, col) in ['-', 'L', 'F', 'S']:
            col -= 1
            last = 'west'
            if not first:
                first = last
        else:
            print('shit')
        loop.append((row, col))
    return (loop, first, last)

def determine_start(first, last):
    result = 'S'
    if first == 'north':
        if last == 'west':
            result = 'L'
        elif last == 'east':
            result = 'J'
        else:
            result = '|'
    elif first == 'east':
        if last == 'north':
            result = 'F'
        else:
            result = '-'
    else:
        result = '7'
    return result

def visualize(graph, row, col):
    loop, first, last = get_loop(graph, row, col)
    graph[row][col] = determine_start(first, last)
    # Anything non-loop is a .
    for row in range(len(graph)):
        line = ''.join(graph[row])
        for col in range(len(graph[row])):
            ch = graph[row][col]
            if (row, col) in loop:
                if ch == 'F':
                    ch = u'\u250c'
                elif ch == '7':
                    ch = u'\u2510'
                elif ch == 'L':
                    ch = u'\u2514'
                elif ch == 'J':
                    ch = u'\u2518'
                elif ch == '-':
                    ch = u'\u2500'
                elif ch == '|':
                    ch = u'\u2502'
            else:
                ch = '.'
                if (line[:col].count('|') + line[:col].count('L') + line[:col].count('J')) % 2 > 0:
                    ch = '*'
                line = line[:col]+ch+line[col+1:]
            graph[row][col] = ch
    for line in graph:
        print(''.join(line))

def result_a(graph, row, col):
    return len(get_loop(graph, row, col)[0]) // 2

def result_b(graph, row, col):
    result = 0
    loop, first, last = get_loop(graph, row, col)
    graph[row][col] = determine_start(first, last)
    # Anything non-loop is a .
    for row in range(len(graph)):
        for col in range(len(graph[row])):
            if (row, col) not in loop:
                graph[row][col] = '.'
    # Simplify
    for line in graph:
        line = ''.join(line).replace('-', '').replace('F7', '').replace('LJ', '').strip('.').replace('L7', '|').replace('FJ', '|')
        # Use parity
        if '.' in line:
            for i, ch in enumerate(line):
                if ch == '.' and line[:i].count('|') % 2 > 0:
                    result += 1
    return result

if __name__ == '__main__':
    with open('input/input10.txt') as input:
        graph = []
        for row, line in enumerate(input.read().splitlines()):
            if 'S' in line:
                start_row, start_col = row, line.index('S')
            graph.append(list(line))
        print(result_a(graph, start_row, start_col), result_b(graph, start_row, start_col))
        graph[start_row][start_col] = 'S'
        visualize(graph, start_row, start_col)
