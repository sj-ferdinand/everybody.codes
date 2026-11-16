#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

outposts = [int(_) for _ in notes[0].split(",")]
total = 0
squares = [-1, -1]

def nextSquare(n: int) -> int:
    global squares
    while n > squares[-1]:
        if len(squares) % 2 == 1:
            squares.append((len(squares) ** 2) - 1)
        else:
            squares.append(-1)
    for f in squares:
        if n > f: 
            pass
        else: 
            return f
    raise Exception("no square found") 

def distToNextSquare(n: int) -> int:
    o = nextSquare(n) - n
    return o


for outpost in outposts:
    total += distToNextSquare(outpost)

print(total)