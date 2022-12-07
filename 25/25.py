#!/usr/bin/env python

from collections import defaultdict
import sys
import math
import copy

f = open(sys.argv[1], "r")
#f = open("initial.raw", "r")
map = [[c for c in line] for line in f.read().splitlines()]

print(map)

W = len(map[0])
H = len(map)

loop = 0
moved = True
while moved:
    moved = False
    newmap = copy.deepcopy(map)
    for y in range(H):
        for x in range(W):
            if map[y][x] == ">" and map[y][(x+1)%W]==".":
                newmap[y][x] = "."
                newmap[y][(x+1)%W]=">"
                moved = True
    map = newmap
    newmap = copy.deepcopy(map)
    for y in range(H):
        for x in range(W):
            if map[y][x] == "v" and map[(y+1)%H][x]==".":
                newmap[y][x] = "."
                newmap[(y+1)%H][x]="v"
                moved = True
    map = newmap
    #print(map)
    loop += 1
print(loop)
