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

knots = 0
for i in range(1, len(threads)):
    for j in range(i):
        if ((threads[j][0] > threads[i][0] and threads[j][0] < threads[i][1]) and \
            (threads[j][1] < threads[i][0] or threads[j][1] > threads[i][1])) or \
            ((threads[j][1] > threads[i][0] and threads[j][1] < threads[i][1]) and \
            (threads[j][0] < threads[i][0] or threads[j][0] > threads[i][1])):
            knots += 1

print(knots)