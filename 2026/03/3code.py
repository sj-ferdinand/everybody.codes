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
        b: int = i % len(bases)
        count += votes[i] * (bases[b] ** i)

    valid = True
    vint = int(w.split(" ")[1])
    print(vint, end="")
    for y in range(vint):
        ylst: list[int] = [int(x) for x in str(y)[::-1]]
        
        tc = 0
        for i in range(len(ylst)):
            b: int = i % len(bases)
            tc += ylst[i] * (bases[b] ** i)
        if tc == count:
            valid = False
            print("!", end="")
            break
    if valid:
        total += count
    print("")

    

print(total)