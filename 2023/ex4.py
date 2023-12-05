#!/usr/bin/python3

def get_resultA(cards):
    result = 0
    for _, winners in cards.items():
        if winners > 0:
            result += 2 ** (winners-1)
    return result

def get_resultB(cards):
    result = 0
    num_cards = {n: 1 for n in cards}
    for id, winners in cards.items():
        if winners > 0:
            for i in range(id + 1, id + 1 + winners):
                num_cards[i] += num_cards[id]
    return sum(num_cards.values())

if __name__ == '__main__':
    with open('input/input4.txt') as input:
        scoreA, scoreB = 0, 0
        cards = {}
        for line in input.read().splitlines():
            id, nums = line.split(':')
            id = int(id.replace('Card ', ''))
            theirs = set([int(n) for n in nums.split('|')[0].split()])
            mine = set([int(n) for n in nums.split('|')[1].split()])
            winners = len(theirs & mine)
            cards[id] = winners
        print(get_resultA(cards), get_resultB(cards))
