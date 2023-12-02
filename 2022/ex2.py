#!/usr/bin/python3

def pick(target, goal):
    if goal == 'Y':
        # Draw
        return chr(ord(target)+23)
    if goal == 'Z':
        # Win
        if target == 'A':
            return 'Y'
        if target == 'B':
            return 'Z'
        return 'X'
    # Lose
    if target == 'A':
        return 'Z'
    if target == 'B':
        return 'X'
    return 'Y'

def score(them, us):
    # Our pick
    score = ord(us)-87
    # Round result
    adj_us = chr(ord(us)-23)
    if adj_us == them:
        score += 3
    elif ord(adj_us) == ord(them)+1 or ord(adj_us) == ord(them)-2:
        score += 6
    return score

with open('input2.txt') as input:
    a_score = 0
    b_score = 0
    for line in input.read().splitlines():
        (opp, res) = line.split()
        a_score += score(opp, res)
        b_score += score(opp, pick(opp, res))
    print(a_score)
    print(b_score)
