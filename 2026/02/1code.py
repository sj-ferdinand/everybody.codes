#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

total = 0

for group in notes:
    comps = [c.strip() for c in group.split(" ")]
    for i in range(len(comps)):
        comp = comps[i]
        if comp[1] == "<":
            comps[i] = f"{comp[2]}>{comp[0]}"
    
    items: set[int] = set()
    for comp in comps:
        items.add(int(comp[0]))
        items.add(int(comp[2]))

    smallers: list[int] = [int(c[2]) for c in comps]
    smallerCount: dict[int, int] = dict()
    for i in items:
        smallerCount[i] = smallers.count(i)

    itemsSorted: list[int] = list(items)
    itemsSorted.sort(key = lambda x: smallerCount[x])
    
    csumStr = ""
    for i in itemsSorted: csumStr += str(i)
    csum = int(csumStr)

    total += csum
    pass

print(total)