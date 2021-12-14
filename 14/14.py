#!/usr/bin/env python

import sys
from collections import defaultdict

f = open(sys.argv[1], "r")
initial = f.readline().strip()
f.readline()

poly = dict()
while line := f.readline().strip():
    values = line.split(" -> ")
    poly[values[0]] = values[1]

freq = defaultdict(int)
for i in range(1, len(initial)):
    freq[initial[i-1:i+1]] += 1

loops = int(sys.argv[2])
for l in range(loops):
    newfreq = defaultdict(int)
    for source, quantity in freq.items():
        ins = poly[source]
        newfreq[source[0]+ins] += quantity
        newfreq[ins+source[1]] += quantity
    freq = newfreq

# now count
elems = defaultdict(int)
for source, quantity in freq.items():
    elems[source[0]] += quantity
    elems[source[1]] += quantity
# Beware! All are double-counted except first and last on the chain (that remain constant)
elems[initial[0]] += 1
elems[initial[-1]] += 1

values = list(elems.values())
values.sort()
print((values[-1]-values[0])//2)
