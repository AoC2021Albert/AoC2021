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

manualopt = {
    "((((S0+2)%26)+15)==S1)": "0",
    "((((((S0+2)*26)+(S1+16))%26)+14)==S2)": "0",
    "((((((((S0+2)*26)+(S1+16))*26)+(S2+9))%26)+15)==S3)": "0",
    "((((((((((S0+2)*26)+(S1+16))*26)+(S2+9))*26)+S3)%26)+-8)==S4)": "S101",
}


def myisdecimal(x):
    if x[0] == "-":
        x = x[1:]
    return(str.isdecimal(x))


def fadd(x, y):
    if myisdecimal(x) and myisdecimal(y):
        return(str(int(x)+int(y)))
    elif x == "0":
        return(y)
    elif y == "0":
        return(x)
    else:
        return("("+x+"+"+y+")")


def fmul(x, y):
    if myisdecimal(x) and myisdecimal(y):
        return(str(int(x)*int(y)))
    elif x == "0" or y == "0":
        return("0")
    elif x == "1":
        return(y)
    elif y == "1":
        return(x)
    else:
        return("("+x+"*"+y+")")


def fdiv(x, y):
    if myisdecimal(x) and myisdecimal(y):
        return(str(int(x)//int(y)))
    elif x == "0":
        return("0")
    elif y == "1":
        return(x)
    else:
        return("("+x+"/"+y+")")


def fmod(x, y):
    if myisdecimal(x) and myisdecimal(y):
        return(str(int(x) % int(y)))
    elif x == "0":
        return("0")
    else:
        return("("+x+"%"+y+")")


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


def monad(digits):
    digitcount = 0
    for opline in ops:
        print(reg, opline)
        op = opline[0]
        dreg = opline[1]
        if op == "inp":
            reg[dreg] = digits[digitcount]
            digitcount += 1
            print(digitcount)
        else:
            value = opline[2]
            if value in ["w", "x", "y", "z"]:
                reg[dreg] = callopr[op](reg[dreg], reg[value])
            else:
                reg[dreg] = callopr[op](reg[dreg], value)
            if reg[dreg] in manualopt.keys():
                reg[dreg] = manualopt[reg[dreg]]
    return(reg["z"])


digits = "99999999999999"
print(monad(digits))
