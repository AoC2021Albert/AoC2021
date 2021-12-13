#!/usr/bin/env python

from collections import defaultdict

f = open("in.raw", "r")
conn = [[p for p in row.split("-")] for row in f.read().splitlines()]
allc = defaultdict(lambda: [])
for c in conn:
    allc[c[0]].append(c[1])
    allc[c[1]].append(c[0])


def to_end(current, visited, can_repeat):
    if current == "end":
        return(1)
    if current == "start" and visited:
        return(0)
    ways = 0
    for next in allc[current]:
        repetition = next.islower() and (next in visited)
        if can_repeat or (not repetition):
            ways += to_end(next, visited+[next],
                           (not repetition) and can_repeat)
    return(ways)


print(to_end("start", [], False))
print(to_end("start", [], True))
