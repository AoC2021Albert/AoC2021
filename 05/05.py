#!/usr/bin/env python

from collections import defaultdict
import math

X = 0
Y = 1
f = open("in.raw", "r")
lines = f.read().splitlines()

m = defaultdict(lambda: defaultdict(int))  # m[x][y]=vents_count_here
for line in lines:
    org, dst = line.split(" -> ")
    org = [int(n) for n in org.split(",")]
    dst = [int(n) for n in dst.split(",")]
    if org[X] == dst[X]:
        orgy, dsty = org[Y], dst[Y]
        if orgy > dsty:
            orgy, dsty = dsty, orgy
        for y in range(orgy, dsty+1):
            m[org[X]][y] += 1
    elif org[Y] == dst[Y]:
        orgx, dstx = org[X], dst[X]
        if orgx > dstx:
            orgx, dstx = dstx, orgx
        for x in range(orgx, dstx+1):
            m[x][org[Y]] += 1
    # part 2
    else:
        lenx = dst[X]-org[X]
        leny = dst[Y]-org[Y]
        sigx = int(math.copysign(1, lenx))
        sigy = int(math.copysign(1, leny))
        if abs(lenx) == abs(leny):
            y = org[Y]
            for x in range(org[X], dst[X] + sigx, sigx):
                m[x][y] += 1
                y += sigy

# print(m)
print(sum(sum(1 if v > 1 else 0 for v in row.values()) for row in m.values()))
