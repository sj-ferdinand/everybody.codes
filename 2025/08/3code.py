#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

nailSeq = [int(n) for n in notes[0].strip().split(',')]
nailCount = 256

threads = []
for i in range(len(nailSeq) - 1):
    a = min(nailSeq[i], nailSeq[i + 1])
    b = max(nailSeq[i], nailSeq[i + 1])

    threads.append((a, b))

maxKnots = 0

for i in range(len(threads)):
    
    for j in range(1, nailCount + 1):
        knots = 0
        for k in range(j, nailCount + 1):
            print(f'{maxKnots} {i}/{len(threads)} {j} {k}')
            if ((j > threads[i][0] and j < threads[i][1]) and \
                (k < threads[i][0] or k > threads[i][1])) or \
                ((k > threads[i][0] and k < threads[i][1]) and \
                (j < threads[i][0] or j > threads[i][1])) or \
                (j == threads[i][0] and k == threads[i][1]):
                knots += 1
            if knots > maxKnots: 
                maxKnots = knots

print(maxKnots)