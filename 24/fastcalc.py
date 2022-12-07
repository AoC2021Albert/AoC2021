#!/usr/bin/env python
# 9 anys!!
import sys

DIV = [1,   1,  1,  1, 26,  1,  26, 26,  1, 26,  1, 26,  26, 26]
N1 = [10, 15, 14, 15, -8, 10, -16, -4, 11, -3, 12, -7, -15, -7]
N2 = [2,  16,  9,  0,  1, 12,   6,  6,  3,  5,  9,  3,   2,  3]


for inp in range(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])):
    digits = [int(c) for c in "{:014d}".format(inp)]
    z = 0
    for i in range(14):
        w = digits[i]
        if (z % 26+N1[i] != w):
            z = z // DIV[i]
            z = z * 26 + w + N2[i]
        else:
            z = z // DIV[i]
            z = z + w
    print(inp, z)
    if z == 0:
        print(inp)
        exit()
    if inp % 1000000 == 0:
        print(inp)
