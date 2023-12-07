#!/usr/bin/python3

from collections import Counter

orderA = {'2': 12, '3': 13, '4': 14, '5': 15, '6': 16, '7': 17, '8': 18, '9': 19, 'T': 20, 'J': 21, 'Q': 22, 'K': 23, 'A': 24}
orderB = {'J': 00, '2': 12, '3': 13, '4': 14, '5': 15, '6': 16, '7': 17, '8': 18, '9': 19, 'T': 20, 'Q': 22, 'K': 23, 'A': 24}

def hand_sort(hand):
    val = []
    for card in hand[1]:
        val.append(str(orderA.get(card)))
    return (hand[0], val)

def hand_sort_b(hand):
    val = []
    for card in hand[1]:
        val.append(str(orderB.get(card)))
    return (hand[0], val)

def rank(cards, mode):
    ctr = Counter(cards)
    if mode == 'B' and 'J' in cards:
        j_val = ctr['J']
        del ctr['J']
        if j_val == 5:
            ctr['2'] = j_val
        else:
            # shame, shame
            if len(ctr.most_common()) > 1 and ctr.most_common()[0][1] == ctr.most_common()[1][1]:
                a, b = orderB[ctr.most_common()[0][0]], orderB[ctr.most_common()[1][0]]
                if b > a:
                    ctr[ctr.most_common()[1][0]] += j_val
                else:
                    ctr[ctr.most_common()[0][0]] += j_val
            else:
                ctr[ctr.most_common()[0][0]] += j_val
    ctr_lst = list(ctr.values())
    if 5 in ctr_lst:
        rank = 6
    elif 4 in ctr_lst:
        rank = 5
    elif 3 in ctr_lst and 2 in ctr_lst:
        rank = 4
    elif 3 in ctr_lst:
        rank = 3
    elif ctr_lst.count(2) == 2:
        rank = 2
    elif 2 in ctr_lst:
        rank = 1
    else:
        rank = 0
    return rank

def get_resultA(hands):
    result = 0
    hands.sort(reverse=True, key=hand_sort)
    for i in range(len(hands)):
        handrank = len(hands)-i
        result += handrank * hands[i][2]
    return result

def get_resultB(hands):
    result = 0
    hands.sort(reverse=True, key=hand_sort_b)
    for i in range(len(hands)):
        handrank = len(hands)-i
        result += handrank * hands[i][2]
    return result

if __name__ == '__main__':
    with open('input/input7.txt') as input:
        handsA, handsB = [], []
        for line in input:
            cards, bid = line.split()
            handsA.append((rank(cards, 'A'), cards, int(bid)))
            handsB.append((rank(cards, 'B'), cards, int(bid)))
        print(get_resultA(handsA), get_resultB(handsB))
