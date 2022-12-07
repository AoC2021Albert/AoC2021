#!/usr/bin/env python

import sys
import re

f = open("in.raw", "r")
ops = [line.split(" ") for line in f.read().splitlines()]
reg = {
    "w": "0",
    "x": "0",
    "y": "0",
    "z": "0"
}


def fadd(x, y):
    return(str(int(x)+int(y)))


def fmul(x, y):
    return(str(int(x)*int(y)))


def fdiv(x, y):
    return(str(int(x)//int(y)))


def fmod(x, y):
    return(str(int(x) % int(y)))


def feql(x, y):
    if x == y:
        return("1")
    else:
        return("0")


callopr = {
    "add": fadd,
    "mul": fmul,
    "div": fdiv,
    "mod": fmod,
    "eql": feql
}

digitcount = 0
for opline in ops:
    print(reg, opline)
    op = opline[0]
    dreg = opline[1]
    if op == "inp":
        reg[dreg] = sys.argv[1][digitcount]
        digitcount += 1
        print(digitcount)
    else:
        value = opline[2]
        if value in ["w", "x", "y", "z"]:
            reg[dreg] = callopr[op](reg[dreg], reg[value])
        else:
            reg[dreg] = callopr[op](reg[dreg], value)

print(reg["z"])
