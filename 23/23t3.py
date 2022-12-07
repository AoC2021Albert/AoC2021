#!/usr/bin/env python

from functools import lru_cache
from collections import defaultdict
from copy import deepcopy

rooms = {
    "A": ["C", "D"],
    "B": ["A", "B"],
    "C": ["A", "D"],
    "D": ["C", "B"]
}
DEPTH = len(rooms["A"])

value = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000,
}

corridors = ["", "", "", "", "", "", ""]
mincost = 99999999999999999999999999999999999999

roomtoroomrange = {
    "AB": range(2, 3),
    "AC": range(2, 4),
    "AD": range(2, 5),
    "BC": range(3, 4),
    "BD": range(3, 5),
    "CD": range(4, 5),
    "BA": range(2, 3),
    "CA": range(2, 4),
    "DA": range(2, 5),
    "CB": range(3, 4),
    "DB": range(3, 5),
    "DC": range(4, 5)
}
# 01 2 3 4 56
#  A B C D
corridortoroomrange = {
    "0A": (1, 2),
    "0B": (1, 3),
    "0C": (1, 4),
    "0D": (1, 5),
    "1A": (2, 2),
    "1B": (2, 3),
    "1C": (2, 4),
    "1D": (2, 5),
    "2A": (2, 2),
    "2B": (3, 3),
    "2C": (3, 4),
    "2D": (3, 5),
    "3A": (2, 3),
    "3B": (3, 3),
    "3C": (4, 4),
    "3D": (4, 5),
    "4A": (2, 4),
    "4B": (3, 4),
    "4C": (4, 4),
    "4D": (5, 5),
    "5A": (2, 5),
    "5B": (3, 5),
    "5C": (4, 5),
    "5D": (5, 5),
    "6A": (2, 6),
    "6B": (3, 6),
    "6C": (4, 6),
    "6D": (5, 6)
}
# 01 2 3 4 56
#  A B C D
corridortoroomdistance = {
    "0A": 2,
    "0B": 4,
    "0C": 6,
    "0D": 8,
    "1A": 1,
    "1B": 3,
    "1C": 5,
    "1D": 7,
    "2A": 1,
    "2B": 1,
    "2C": 3,
    "2D": 5,
    "3A": 3,
    "3B": 1,
    "3C": 1,
    "3D": 3,
    "4A": 5,
    "4B": 3,
    "4C": 1,
    "4D": 1,
    "5A": 7,
    "5B": 5,
    "5C": 3,
    "5D": 1,
    "6A": 8,
    "6B": 6,
    "6C": 4,
    "6D": 2
}


def roomtoroom(fromroom, toroom, corridors):
    if all([corridors[i] == "" for i in roomtoroomrange[fromroom+toroom]]):
        # free corridor
        return(abs(ord(fromroom)-ord(toroom))*2 + 1)
    else:
        return(9999999999999999999999999999999999999999999999999999999999999999999999999)


def corridortoroom(corridors, i):
    ctrr = corridortoroomrange[str(i)+corridors[i]]
    if all([corridors[i] == "" for i in range(ctrr[0], ctrr[1])]):
        return(corridortoroomdistance[str(i)+corridors[i]])
    else:
        return(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)


destleft = {
    "A": [(1, 1), (0, 2)],
    "B": [(2, 1), (1, 3), (0, 4)],
    "C": [(3, 1), (2, 3), (1, 5), (0, 6)],
    "D": [(4, 1), (3, 3), (2, 5), (1, 7), (0, 8)]
}

destright = {
    "A": [(2, 1), (3, 3), (4, 5), (5, 7), (6, 8)],
    "B": [(3, 1), (4, 3), (5, 5), (6, 6)],
    "C": [(4, 1), (5, 3), (6, 4)],
    "D": [(5, 1), (6, 2)]
}


def corridordestinations(fromroom, corridors):
    dl = destleft[fromroom][:]
    dr = destright[fromroom][:]
    for d in [dl, dr]:
        p = 0
        while p < len(d):
            if corridors[d[p][0]] != "":
                del d[p:]
            else:
                p += 1
    r = []
    p = 0
    while p < len(dl) or p < len(dr):
        if p < len(dr):
            r.append(dr[p])
        if p < len(dl):
            r.append(dl[p])
        p += 1
    return(r)


memo = defaultdict(lambda: 9999999999999999999999999999999999)
# @lru_cache(maxsize=16216200)


def solve(rooms, corridors, costsofar):
    sparam = (rooms, corridors, costsofar).__str__()
    if memo[sparam] > costsofar:
        memo[sparam] = costsofar
        distance = 0
        global mincost
        if costsofar >= mincost:
            return(costsofar)
        if (
            rooms["A"] == ["A"] * DEPTH and
            rooms["B"] == ["B"] * DEPTH and
            rooms["C"] == ["C"] * DEPTH and
            rooms["D"] == ["D"] * DEPTH
        ):
            print("new minimum", costsofar)
            mincost = costsofar
        corridorcandidates = []
        for fromroom in rooms.keys():
            if rooms[fromroom]:
                if rooms[fromroom] in ([fromroom],
                                       [fromroom, fromroom]):
                    # skip it, it is fine!
                    ...
                else:
                    toroom = rooms[fromroom][-1]
                    if rooms[toroom] in ([],
                                         [toroom]):
                        distance = roomtoroom(fromroom, toroom, corridors)
                        distance += DEPTH - len(rooms[fromroom])
                        distance += DEPTH - len(rooms[toroom])
                        newrooms = deepcopy(rooms)
                        newcorridors = corridors[:]
                        newrooms[toroom].append(newrooms[fromroom].pop())
                        solve(newrooms, newcorridors,
                              costsofar+distance*value[toroom])
                    else:
                        corridorcandidates.append(fromroom)
        for i, c in enumerate(corridors):
            if c != "" and (rooms[c] in ([], [c])):
                distance = corridortoroom(corridors, i)
                distance += DEPTH - len(rooms[c])
                newrooms = deepcopy(rooms)
                newcorridors = corridors[:]
                newrooms[c].append(c)
                newcorridors[i] = ""
                solve(newrooms, newcorridors, costsofar+distance*value[c])
        for fromroom in corridorcandidates:
            for corridordestionation, distance in corridordestinations(fromroom, corridors):
                distance += DEPTH + 1 - len(rooms[fromroom])
                newrooms = deepcopy(rooms)
                newcorridors = corridors[:]
                newcorridors[corridordestionation] = newrooms[fromroom].pop()
                solve(newrooms, newcorridors, costsofar+distance *
                      value[newcorridors[corridordestionation]])


solve(rooms, corridors, 0)
print(mincost)
