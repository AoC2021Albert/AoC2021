#!/usr/bin/env python

f = open("in.raw", "r")
rows = [[int(v) for v in list(row)] for row in f.read().splitlines()]

width = len(rows[0])
height = len(rows)
BORDER = -1000000000

rows = [[BORDER] * (width + 2)] + \
       [[BORDER] + row + [BORDER] for row in rows] + \
       [[BORDER] * (width + 2)]


def increase(x, y):
    global flashes
    rows[y][x] += 1
    if rows[y][x] == 10:
        for neighbours in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            increase(x + neighbours[0], y + neighbours[1])


p1steps = 100
steps = 0
flashes = 0
loopflashes = 0

while loopflashes < 100:
    loopflashes = 0
    for y in range(1, height + 1):
        for x in range(1, width + 1):
            increase(x, y)
    for y in range(1, height + 1):
        for x in range(1, width + 1):
            if rows[y][x] > 9:
                loopflashes += 1
                rows[y][x] = 0
    flashes += loopflashes
    steps += 1
    if steps == p1steps:
        print(flashes)

print(steps)
