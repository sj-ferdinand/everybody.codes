#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

nailSeq = [int(n) for n in notes[0].strip().split(',')]
nailCount = 32

centreCrossings = 0

for i in range(len(nailSeq) - 1):
    if abs(nailSeq[i] - nailSeq[i + 1]) == nailCount / 2:
        centreCrossings += 1

print(centreCrossings)