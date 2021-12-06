#!/usr/bin/env python

from sys import stdin
from collections import defaultdict

lines = stdin.read().splitlines()
total = len(lines)
l = len(lines[0])

# part 1
out = []
for p in range(l):
    out.append(0 if (sum([int(line[p])
               for line in lines]) < (total / 2)) else 1)
print(out)
gamma = int("".join((str(d) for d in out)), 2)
epsilon = pow(2, l)-gamma-1
print(epsilon * gamma)

# oxigen
ox = lines[:]
p = 0
while len(ox) > 1:
    ox.sort()
    c = 0
    while ox[c][p] == "0":
        c += 1
    if c * 1.0 <= len(ox) / 2:
        ox = ox[c:]
    else:
        if c < len(ox):
            ox = ox[:c]
    p += 1
print(ox)
oxn = int("".join((str(d) for d in ox)), 2)

# co2
co2 = lines[:]
p = 0
while len(co2) > 1:
    co2.sort()
    c = 0
    while co2[c][p] == "0":
        c += 1
    if c * 1.0 <= len(co2) / 2:
        if c > 0:
            co2 = co2[:c]
    else:
        co2 = co2[c:]
    p += 1
print(co2)
co2n = int("".join((str(d) for d in co2)), 2)

print(co2n * oxn)
