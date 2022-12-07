#!/usr/bin/env python

from collections import defaultdict
import sys
import math
import copy

# cubes will be an array
# each element will be an "on" cube
# there will be no overlaps
cubes = []


def removenewfromold(cubes, newcube, oldcube):
    #print("remove", newcube, "from", oldcube)
    # modifies "cubes" in place
    newcubes = []
    currentcube = copy.deepcopy(oldcube)
    for d in range(3):
        if max(newcube[0][d], currentcube[0][d]) <= min(newcube[1][d], currentcube[1][d]):
            # We got an intersection on this dimension
            fourpointlist = [(newcube[0][d], "new"),
                             (newcube[1][d], "new"),
                             (currentcube[0][d], "old"),
                             (currentcube[1][d], "old")]
            fourpointlist.sort()
            # Dimension dim overlaps
            # so we have 3 segments
            # 0-1 1-2 2-3
            segone = fourpointlist[0][0], fourpointlist[1][0]-1
            segtwo = fourpointlist[1][0], fourpointlist[2][0]
            segthree = fourpointlist[2][0]+1, fourpointlist[3][0]

            # if segment 0-1 has content (it could be an overlap!)
            # and point "0" had to be on, then we have an "on segment"
            if segone[0] <= segone[1] and fourpointlist[0][1] == "old":
                remain = copy.deepcopy(currentcube)
                remain[1][d] = segone[1]
                newcubes.append(remain)
                currentcube[0][d] = segone[1]+1

            # segment 1-2 always has content. Nothing to do here

            # if segment 2-3 has content (it could be an overlap!)
            # and point "3" has to be on, then we have an "on segment"
            if segthree[0] <= segthree[1] and fourpointlist[3][1] == "old":
                remain = copy.deepcopy(currentcube)
                remain[0][d] = segthree[0]
                newcubes.append(remain)
                currentcube[1][d] = segthree[0]-1
            print("Intersecting", oldcube, " with", newcube, "step", d,
                  "have newcubes", newcubes, "and currentcube", currentcube)
        else:
            # if there is a dimension without intersection, there is no
            # 3D intersection
            return()

    # All three dimensions of newcube are overlaping with oldcube
    # We remove the oldcube and replace it with the newcubes
    ncv = sum(volume(cube) for cube in newcubes)
    ccv = volume(currentcube)
    ocv = volume(oldcube)
    assert(ncv+ccv == ocv)
    cubes.remove(oldcube)
    cubes += newcubes


def addcube(cubes, on, newcube):
    print("addcube", cubes, on, newcube)
    for oldcube in cubes[:]:
        removenewfromold(cubes, newcube, oldcube)
    if on:
        cubes.append(newcube)


def volume(cube):
    return(math.prod([abs(cube[0][d]-cube[1][d])+1 for d in range(3)]))


f = open(sys.argv[1], "r")
#f = open("initial.raw", "r")
lines = f.read().splitlines()

for line in lines:
    on, rest = line.split(' ')
    on = (on == "on")
    ranges = rest.split(',')
    newcube = [[0, 0, 0], [0, 0, 0]]
    for d, axisrange in enumerate(ranges):
        axis, values = axisrange.split('=')
        newcube[0][d], newcube[1][d] = map(int, values.split(".."))
    print(newcube, "has volume", volume(newcube))
    addcube(cubes, on, newcube)
    print("allcubes", cubes, "have volume", sum(volume(cube)
          for cube in cubes))

print(cubes)
print(sum(volume(cube) for cube in cubes))
