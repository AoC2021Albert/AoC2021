#!/usr/bin/env python

f = open("in.raw", "r")
fishes = f.readline().strip().split(",")

bytime = [0]*9
for fish in fishes:
    bytime[int(fish)] += 1

count = 256
for _ in range(count):
    breeding = bytime[0]
    bytime = bytime[1:] + [breeding]
    bytime[6] += breeding
print(sum(bytime))
