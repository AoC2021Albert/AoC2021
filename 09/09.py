#!/usr/bin/env python

f = open("in.raw", "r")
lines = f.read().splitlines()
map = ["9"*(len(lines[0])+2)] + \
      ["9"+line+"9" for line in lines] + \
      ["9"*(len(lines[0])+2)]
for row in map:
    print(row)

# p1
risk = 0

# p2
basinsizes = []
visitedmap = [
    ["X" if r[c] == "9" else "0" for c in range(len(r))] for r in map]
for row in visitedmap:
    print("".join(row))

# scan map
for row in range(1, len(map)):
    for column in range(1, len(map[0])-1):
        # detect basins
        if ((int(map[row - 1][column]) > int(map[row][column])) and
           (int(map[row][column-1]) > int(map[row][column])) and
           (int(map[row][column+1]) > int(map[row][column])) and
           (int(map[row + 1][column]) > int(map[row][column]))):
            risk += int(map[row][column]) + 1
            to_count = {(row, column)}
            basinsize = 0
            while to_count:
                r, c = to_count.pop()
                visitedmap[r][c] = "X"
                basinsize += 1
                for deltar, deltac in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    if (r + deltar > 0) and (c + deltac > 0) and \
                            visitedmap[r+deltar][c+deltac] == "0":
                        to_count.add((r+deltar, c+deltac))
            basinsizes.append(basinsize)

print(risk)
basinsizes.sort(reverse=True)
print(basinsizes[0]*basinsizes[1]*basinsizes[2])

# p2 faster method, no need to detect the basin first

basinsizes = []
visitedmap = [
    ["X" if r[c] == "9" else "0" for c in range(len(r))] for r in map]
for row in range(1, len(map)):
    for column in range(1, len(map[0])-1):
        if visitedmap[row][column] == "0":
            to_count = {(row, column)}
            basinsize = 0
            while to_count:
                r, c = to_count.pop()
                visitedmap[r][c] = "X"
                basinsize += 1
                for deltar, deltac in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    if (r + deltar > 0) and (c + deltac > 0) and \
                            visitedmap[r+deltar][c+deltac] == "0":
                        to_count.add((r+deltar, c+deltac))
            basinsizes.append(basinsize)

basinsizes.sort(reverse=True)
print(basinsizes[0]*basinsizes[1]*basinsizes[2])
