#!/usr/bin/env python

import sys

dotsin = set()


def fold(dir, val):
    global dotsin
    newdotsin = set()
    coord = 0 if dir == "x" else 1
    for dot in dotsin:
        if dot[coord] > val:
            ldot = list(dot)
            ldot[coord] = 2*val - ldot[coord]
            dot = tuple(ldot)
        newdotsin.add(dot)
    dotsin = newdotsin


f = open(sys.argv[1], "r")
line = f.readline()
while "," in line:
    dotsin.add(tuple([int(v) for v in line.split(",")]))
    line = f.readline()

while line := f.readline():
    dir, val = line.split("fold along ")[1].split("=")
    fold(dir, int(val))
    print(len(dotsin))

out = [[" "]*100 for _ in range(20)]

for dot in dotsin:
    out[dot[1]][dot[0]] = "#"
for line in out:
    print("".join(line))
