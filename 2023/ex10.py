#!/usr/bin/python3

def north(graph, row, column):
    return graph[row-1][column] if row > 0 else None

def east(graph, row, column):
    return graph[row][column+1] if len(graph[row]) >= column else None

def south(graph, row, column):
    return graph[row+1][column] if len(graph) >= row else None

def west(graph, row, column):
    return graph[row][column-1] if column > 0 else None

def result_a(graph, row, col):
    steps, last = 0, None
    while steps == 0 or graph[row][col] != 'S':
        steps += 1
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
    return steps // 2

if __name__ == '__main__':
    with open('input/input10.txt') as input:
        result_b = 0
        graph = []
        for row, line in enumerate(input.read().splitlines()):
            if 'S' in line:
                start_row, start_col = row, line.index('S')
            graph.append(line)
        print(result_a(graph, start_row, start_col), result_b)
