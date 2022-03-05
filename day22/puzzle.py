with open("input.txt", "r") as file:
    lines = file.read().splitlines()

instrs = []
for line in lines:
    onoff, rest = line.split(" ")
    onoff = int(onoff == "on")
    x, y, z = rest.split(",")
    minx, maxx = x[2:].split("..")
    miny, maxy = y[2:].split("..")
    minz, maxz = z[2:].split("..")
    instrs.append((onoff, int(minx), int(maxx)+1, int(miny), int(maxy)+1, int(minz), int(maxz)+1))

all_xs = sorted(list(set(n[1] for n in instrs).union(set(n[2] for n in instrs))))
all_ys = sorted(list(set(n[3] for n in instrs).union(set(n[4] for n in instrs))))
all_zs = sorted(list(set(n[5] for n in instrs).union(set(n[6] for n in instrs))))
print(len(all_xs), len(all_ys), len(all_zs))

import numpy as np
grid = np.zeros((len(all_xs)-1, len(all_ys)-1, len(all_zs)-1))

for i, (onoff, x1, x2, y1, y2, z1, z2) in enumerate(instrs):
    print(i)
    xi1 = all_xs.index(x1)
    xi2 = all_xs.index(x2)
    yi1 = all_ys.index(y1)
    yi2 = all_ys.index(y2)
    zi1 = all_zs.index(z1)
    zi2 = all_zs.index(z2)
    for x in range(xi1, xi2):
        for y in range(yi1, yi2):
            for z in range(zi1, zi2):
                grid[x][y][z] = onoff

total = 0
for x in range(len(all_xs)-1):
    print(x)
    for y in range(len(all_ys)-1):
        for z in range(len(all_zs)-1):
            if grid[x][y][z]:
                total += (all_xs[x+1]-all_xs[x])*(all_ys[y+1]-all_ys[y])*(all_zs[z+1]-all_zs[z])
print(total)

# grid = [[[False for _ in range(101)] for _ in range(101)] for _ in range(101)]
# for onoff, x1, x2, y1, y2, z1, z2 in instrs:
#     if not all(-50 <= k <= 50 for k in (x1, x2, y1, y2, z1, z2)): continue
#     for x in range(x1+50, x2+51):
#         for y in range(y1+50, y2+51):
#             for z in range(z1+50, z2+51):
#                 grid[x][y][z] = onoff

# print(sum(grid[x][y][z] for x in range(101) for y in range(101) for z in range(101)))