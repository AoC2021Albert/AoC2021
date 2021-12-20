#!/usr/bin/env python

import sys


def expand(map, border, layers):
    w = len(map[0])
    map = [[border]*(w+(layers*2)) for _ in range(layers)] + \
          [[border for _ in range(layers)] + l + [border for _ in range(layers)] for l in map] + \
          [[border]*(w+(layers*2)) for _ in range(layers)]
    return(map)


def tonum(s):
    return(int("".join(s), 2))


def filter(map, y, x):
    val = map[y-1][x-1:x+2] + \
        map[y][x-1:x+2] + \
        map[y+1][x-1:x+2]
    return(index[tonum(val)])


f = open(sys.argv[1], "r")
lines = f.read().splitlines()
index = ["1" if c == "#" else "0" for c in lines[0]]
map = [["1" if c == "#" else "0" for c in l] for l in lines[2:]]

background = "0"
map = expand(map, background, 2)

for loops in range(int(sys.argv[2])):
    newmap = [[background] * (len(map[0])-2) for _ in range(len(map)-2)]
    background = index[tonum(background*9)]
    for y in range(len(newmap)):
        for x in range(len(newmap[0])):
            newmap[y][x] = filter(map, y+1, x+1)
    map = expand(newmap, background, 2)

print(sum([l.count('1') for l in map]))
