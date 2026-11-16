#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

total = 0
for v in notes:
    w: str = v.split("-")[1].strip()
    bases: list[int] = [int(x) for x in w.split(" ")[0][::-1]]
    votes: list[int] = [int(x) for x in w.split(" ")[1][::-1]]

    count = 0
    for i in range(len(votes)):
        count += votes[i] * (bases[i] ** i)

    total += count

print(total)