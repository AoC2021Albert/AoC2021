#!/usr/bin/env python

import sys
import re

DIV = [1,   1,  1,  1, 26,  1,  26, 26,  1, 26,  1, 26,  26, 26]
N1 = [10, 15, 14, 15, -8, 10, -16, -4, 11, -3, 12, -7, -15, -7]
N2 = [2,  16,  9,  0,  1, 12,   6,  6,  3,  5,  9,  3,   2,  3]

attempting = [0] * 14


def attempt(pos, previousz):
    if pos == 14:
        if previousz == 0:
            print(attempting)
        return()
    if N1[pos] < 0:
        matcher = previousz % 26 + N1[pos]
        if matcher > 0 and matcher < 10:
            attempting[pos] = matcher
            attempt(pos+1, previousz // 26)
        else:
            return()
    else:
        for candidate in range(9, 0, -1):
            attempting[pos] = candidate
            attempt(pos+1, previousz * 26 + N2[pos] + candidate)


attempt(0, 0)
