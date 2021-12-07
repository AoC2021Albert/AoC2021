#!/usr/bin/env python

f = open("in.raw", "r")
crabs = [int(v) for v in f.readline().strip().split(",")]
mincrab = min(crabs)
maxcrab = max(crabs)

result=999999999999999999999999999999999999999999
for p in range(mincrab,maxcrab+1):
  cost = 0
  for q in crabs:
    dist = abs(p - q)
    #p1
    #cost += dist
    #p2
    cost += (dist * (dist +1 )) // 2
  result = min(result, cost)

print(result)

