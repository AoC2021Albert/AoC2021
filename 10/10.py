#!/usr/bin/env python

f = open("in.raw", "r")
lines = f.read().splitlines()

closers = {
    "]": "[",
    "}": "{",
    ")": "(",
    ">": "<"
}

synerrscore = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

incompletescore = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

p1score = 0
p2scores = []
for line in lines:
    stack = []
    synok = True
    for p in line:
        if p in closers:
            if stack and synok:
                last = stack.pop()
                if (closers[p] != last):
                    synok = False
                    p1score += synerrscore[p]
        else:
            stack.append(p)
    if synok:
        p2score = 0
        while stack:
            p2score *= 5
            p2score += incompletescore[stack.pop()]
        p2scores.append(p2score)

print(p1score)
p2scores.sort()
print(p2scores[len(p2scores)//2])
