#!/usr/bin/env python

import sys
import math
from collections import defaultdict

xinitial = 20
xfinal = 30

yinitial = -5
yfinal = -10

maxy = 9

xinitial = 185
xfinal = 221

yinitial = -74
yfinal = -122

maxy = -yfinal

# p1
print(-yfinal * (-yfinal - 1) - ((-yfinal) * ((-yfinal) - 1) // 2))

p2 = 0
for ivx in range(xfinal+1):
    for ivy in range(yfinal, maxy+1):
        x = 0
        y = 0
        dx = ivx
        dy = ivy
        hit = False
        step = 0
        while x < xfinal and y > yfinal and not hit:
            x = x + dx
            y = y + dy
            if x >= xinitial and x <= xfinal and y <= yinitial and y >= yfinal:
                hit = True
            else:
                if dx > 0:
                    dx -= 1
                dy -= 1
        if hit:
            p2 += 1

print(p2)
