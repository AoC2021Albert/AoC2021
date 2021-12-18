#!/usr/bin/env python

import sys
from collections import defaultdict
from copy import deepcopy, copy

def conv(c):
    if c == "[":
        return(-1)
    if c == ",":
        return(-2)
    if c == "]":
        return(-3)
    else:
        return(ord(c) - ord("0"))

def isnum(element):
    return(element>=0)

OPEN = conv("[")
MID = conv(",")
CLOSE = conv("]")

def to_list(s):
    r = [conv(c) for c in s]
    return(r)

def reduce(n):
    cl = 0
    while cl != len(n):
        cl = len(n)
        #check if too nested to explode
        p = 1
        level = 0
        lastnumberpos = 0
        while p < len(n):
            if n[p] == OPEN:
                level += 1
                if level >= 4:
                    #explode. We know that p+1 will be a number, p+2 MID, p+3 a number and p+4 CLOSE
                    left = n[p+1]
                    right = n[p+3]
                    #replace current part with a 0
                    n = n[:p]+[0]+n[p+5:]
                    #add left
                    if lastnumberpos>0:
                        n[lastnumberpos] += left
                    #add right
                    p+=1 #p was pointing to our just introduced "0" now
                    while p < len(n):
                        if isnum(n[p]):
                            n[p]+=right
                            p=len(n)
                        else:
                            p+=1
            elif n[p] == CLOSE:
                level -= 1
            elif n[p] == MID:
                ...
            else: #it is a number
                lastnumberpos = p
            p += 1
        if cl == len(n): #no change in length = no nested pending, so lets split
            p = 0
            while p < len(n):
                if isnum(n[p]) and n[p]>9:
                    n = n[:p] + [OPEN] + [n[p] // 2]  + [MID] + [(n[p]+1) // 2] + [CLOSE] + n[p+1:]
                    p = len(n)
                p+=1
    return(n)

def addition(n1, n2):
    unreduced = ([OPEN] + n1 + [MID] + n2 + [CLOSE])
    return(reduce(unreduced))

def magnitude(n):
    r = 0
    mulfactor = 1
    p = 0
    for elem in n:
        if elem == OPEN:
            mulfactor=mulfactor*3
        elif elem == MID:
            mulfactor=(mulfactor // 3) * 2
        elif elem == CLOSE:
            mulfactor = mulfactor // 2
        else:
            r+= mulfactor*elem
    return(r)

f = open(sys.argv[1], "r")
sfns = f.read().splitlines()

p1 = to_list(sfns[0])

for sfn in sfns[1:]:
    p1 = addition(p1, to_list(sfn))

print(magnitude(p1))

p2 = 0
for i in sfns:
    for j in sfns:
        if i!=j:
            ni = to_list(i)
            nj = to_list(j)
            p2 = max(p2, magnitude(addition(ni,nj)), magnitude(addition(nj,ni)))

print(p2)
