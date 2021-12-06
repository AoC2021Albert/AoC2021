#!/usr/bin/env python

from collections import defaultdict
import re

f = open("in.raw", "r")
drawn = [int(n) for n in f.readline().strip().split(",")]
boards = []
while f.readline():
    rawboard = []
    for r in range(5):
        textrow = re.split(r" +", f.readline().strip())
        rawboard.append([int(n) for n in textrow])
    # Row sets
    boardsets = [set(r) for r in rawboard]
    # Column sets
    for c in range(5):
        boardsets.append(set(int(r[c]) for r in rawboard))
    boards.append(boardsets)
#print(boards)

winner = False
for draw in drawn:
    for boardsets in boards[:]:
        for s in boardsets:
            s.discard(draw)
            if len(s) == 0:
                winner = True

        if winner:
            print(draw * (sum(sum(s) for s in boardsets) // 2))
            # For part 1 exit()
            boards.remove(boardsets)
            winner = False
