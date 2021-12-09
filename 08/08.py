#!/usr/bin/env python

f = open("in.raw", "r")
c = 0
p2 = 0
s5 = []
s6 = []
v = [""] * 10
for line in f.readlines():
    info, value = line.strip().split(" | ")
    infod = info.split(" ")
    valued = value.split(" ")
    for value in valued[:]:
        if len(value) in [2, 3, 4, 7]:
            c += 1

    for value in infod[:]:
        # p2
        if len(value) == 2:
            v[1] = set(value)
        elif len(value) == 3:
            v[7] = set(value)
        elif len(value) == 4:
            v[4] = set(value)
        elif len(value) == 5:
            s5.append(set(value))
        elif len(value) == 6:
            s6.append(set(value))
        elif len(value) == 7:
            v[8] = set(value)
        else:
            exit(1)

    # decoding
    print(s5, v[1])
    for s in s5:
        print(s, v[1].intersection(s))
        print(len(v[1].intersection(s)))
        if len(v[1].intersection(s)) == 2:
            v[3] = s
    print(s5, v[3])
    s5.remove(v[3])
    for s in s5:
        if len(v[4].intersection(s)) == 3:
            v[5] = s
    s5.remove(v[5])
    v[2] = s5.pop()

    for s in s6:
        if len(v[4].intersection(s)) == 4:
            v[9] = s
    s6.remove(v[9])
    for s in s6:
        if len(v[1].intersection(s)) == 2:
            v[0] = s
    s6.remove(v[0])
    v[6] = s6.pop()
    print(v)

    n = 0
    for d in valued:
        n = n*10+v.index(set(d))
    p2 += n

print(c)
print(p2)
