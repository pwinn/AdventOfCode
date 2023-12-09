#!/usr/bin/python3

def find_next(values):
	next = []
	if sum(val != 0 for val in values) == 0:
		return 0
	for i in range(len(values)-1):
		next.append(values[i+1] - values[i])
	return values[-1] + find_next(next)

if __name__ == '__main__':
    with open('input/input9.txt') as input:
        result_a, result_b = 0, 0
        for line in input.read().splitlines():
            values = [int(n) for n in line.split()]
            result_a += find_next(values)
            result_b += find_next(values[::-1])
        print(result_a, result_b)
