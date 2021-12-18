#!/usr/bin/env python

import sys
from collections import defaultdict
from copy import deepcopy, copy


class StringReader:
    def __init__(self, s):
        self.s = s

    def read(self):
        r = self.s[0]
        self.s = self.s[1:]
        return(r)

    def peek(self):
        return(self.s[0])

    def eof(self):
        return(len(self.s) == 0)


class SFN:
    def __init__(self, s=None):
        def _parseelement(s):
            if s.peek() == "[":
                return(SFN(s))
            else:
                r = 0
                while(s.peek() not in ("]", ",")):
                    r *= 10
                    r += int(s.read())
                return(r)
        if s:
            assert(s.read() == "[")
            self.left = _parseelement(s)
            assert(s.read() == ",")
            self.right = _parseelement(s)
            assert(s.read() == "]")
        else:
            self.left = None
            self.right = None

    def __repr__(self):
        return("[" + self.left.__repr__() + "," + self.right.__repr__() + "]")

    def add(self, added):
        if self.left:
            self.left = deepcopy(self)
            self.right = deepcopy(added)
            self._reduce()
        else:
            self.left = added.left
            self.right = added.right

    def addleft(self, value):
        if isinstance(self.left, SFN):
            self.left.addleft(value)
        else:
            self.left += value

    def addright(self, value):
        if isinstance(self.right, SFN):
            self.right.addright(value)
        else:
            self.right += value

    def explode(self, n):
        if n == 0:
            # we have two numbers under us
            return(True, 0, self.left, self.right)
        else:
            spillleft = None
            spillright = None
            exploding = False
            if isinstance(self.left, SFN):
                exploding, newleft, spillleft, spillright = self.left.explode(
                    n-1)
                self.left = newleft
                if exploding and spillright:
                    if isinstance(self.right, SFN):
                        self.right.addleft(spillright)
                    else:
                        self.right += spillright
                    spillright = None
            if not exploding and isinstance(self.right, SFN):
                exploding, newright, spillleft, spillright = self.right.explode(
                    n-1)
                self.right = newright
                if exploding and spillleft:
                    if isinstance(self.left, SFN):
                        self.left.addright(spillleft)
                    else:
                        self.left += spillleft
                    spillleft = None
            return(exploding, self, spillleft, spillright)

    def split(self):
        splitting = False
        if isinstance(self.left, SFN):
            splitting = self.left.split()
        else:
            if self.left > 9:
                self.left = SFN(StringReader(
                    "[" + str(self.left // 2) + "," + str((self.left + 1) // 2) + "]"))
                splitting = True
        if not splitting:
            if isinstance(self.right, SFN):
                splitting = self.right.split()
            else:
                if self.right > 9:
                    self.right = SFN(StringReader(
                        "[" + str(self.right // 2) + "," + str((self.right + 1) // 2) + "]"))
                    splitting = True
        return(splitting)

    def _reduce(self):
        while self.explode(4)[0] or self.split():
            ...

    def magnitude(self):
        r = 0
        if isinstance(self.left, SFN):
            r += 3 * self.left.magnitude()
        else:
            r += 3 * self.left
        if isinstance(self.right, SFN):
            r += 2 * self.right.magnitude()
        else:
            r += 2 * self.right
        return(r)


f = open(sys.argv[1], "r")
sfns = [SFN(StringReader(line)) for line in f.read().splitlines()]

p1 = SFN()

for sfn in sfns:
    p1.add(copy(sfn))

print(p1.magnitude())

p2 = 0
for i in range(len(sfns)):
    for j in range(len(sfns)):
        if i != j:
            candidate = copy(sfns[i])
            candidate.add(sfns[j])
            p2 = max(p2, candidate.magnitude())
            candidate = copy(sfns[j])
            candidate.add(sfns[i])
            p2 = max(p2, candidate.magnitude())

print(p2)
