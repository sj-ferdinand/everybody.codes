#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

outposts = [int(_) for _ in notes[0].split(",")]
total = 0
squares = [0]

def nextSquare(n: int) -> int:
    global squares
    while n > squares[-1]:
        squares.append(len(squares) ** 2)
    for s in squares:
        if n > s: 
            pass
        else: 
            return s

def distToNextSquare(n: int) -> int:
    o = nextSquare(n) - n
    return o


for outpost in outposts:
    total += distToNextSquare(outpost)

print(total)