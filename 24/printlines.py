#!/usr/bin/env python

import sys
import re

f = open("in.raw", "r")
ops = f.read().splitlines()

for i in range(18):
    print([ops[j*18+i] for j in range(14)])
