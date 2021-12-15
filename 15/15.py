#!/usr/bin/env python

import sys
from collections import defaultdict
MAXVALUE=99999

f = open(sys.argv[1], "r")
map = [[int(v) for v in list(line)] for line in f.read().splitlines()] 

def solve(map):
    H = len(map)
    W = len(map[0])

    # Surround the original map with MAXVALUE to avoid limit checking
    map = [[MAXVALUE]*(W+2)]+ \
          [[MAXVALUE]+l+[MAXVALUE] for l in map]+ \
          [[MAXVALUE]*(W+2)]

    # Create initial map of minimum risk with MAXVALUE (surrounded to avoid limit checking)
    minrisk = [[-1]*(W+2)]+ \
              [[-1]+[MAXVALUE] * W + [-1] for _ in range(H)]  + \
              [[-1]*(W+2)]

    # This will contain lists of coordinates with the same risk from origin
    # indexed by the risk from origi
    pointsbyrisk = defaultdict(list)

    # We start knowing that point 1,1 is at risk 0
    minrisk[1][1] = 0
    pointsbyrisk[0] = [(1,1)]

    currentrisk = 0

    # We loop forever while incrementing currentrisk
    while True:
        while pointsbyrisk[currentrisk]:
            y,x=pointsbyrisk[currentrisk].pop()
            for dir in ([1,0],[0,1],[-1,0],[0,-1]):
                ny = y+dir[0]
                nx = x+dir[1]
                oldrisk = minrisk[ny][nx]
                newrisk = minrisk[y][x] + map[ny][nx]
                if newrisk < oldrisk:
                    # First time we reach our destination we are guaranteed to have minimum risk
                    if ny==H and nx==W:
                        return(newrisk)
                    minrisk[ny][nx] = newrisk
                    pointsbyrisk[newrisk].append((ny,nx))
                    # Not necessary, but some housekeeping
                    if oldrisk != MAXVALUE:
                        pointsbyrisk[oldrisk].remove((y,x))
        currentrisk += 1        

print(solve(map))

H = len(map)
W = len(map[0])

p2map = [[0]*W*5 for _ in range(H*5)]
for y in range(H):
    for x in range(W):
        for ny in range(5):
            for nx in range(5):
                nv = map[y][x]+(ny+nx)
                if nv>9:
                    nv -= 9
                p2map[ny*H+y][nx*W+x] = nv

print(solve(p2map))
