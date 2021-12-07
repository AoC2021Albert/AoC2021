#!/usr/bin/env python

f = open("in.raw", "r")
crabs = [int(v) for v in f.readline().strip().split(",")]

crabs.sort()
upcost=[0]*(crabs[-1]+1)
downcost=[0]*(crabs[-1]+1)

going_up=0
steps=0
for p in range(crabs[-1]+1):
  while (crabs[going_up]<p) and (going_up<len(crabs)):
    going_up+=1
  steps+=going_up
  upcost[p]=steps

going_down=0
steps=0
for p in range(crabs[-1], crabs[0]-1, -1):
  while (crabs[len(crabs)-1-going_down]>p) and (going_down<len(crabs)):
    going_down+=1
  steps+=going_down
  downcost[p]=steps

print(min([(downcost[p]+upcost[p]) for p in range(crabs[-1]+1)]))

result=999999999999999999999999999999999999999999
for p in range(crabs[0],crabs[-1]+1):
  cost = 0
  for q in crabs:
    dist = abs(p - q)
    cost += (dist * (dist +1 )) // 2
  if cost < result:
    result = cost

print(result)

