with open("input.txt", "r") as file:
    lines = file.read().split("\n\n")

import numpy as np

lines = [line.split("\n")[1:] for line in lines]
scanners = [[tuple(map(int, k.split(","))) for k in line] for line in lines]

AMT = len(scanners)

print(scanners[0])

lambdas = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (-y, -z, x),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (y, -z, -x),
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (-z, -x, y),
    lambda x, y, z: (-z, x, -y),
    lambda x, y, z: (z, -x, -y),
    lambda x, y, z: (x, z, -y),
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (-x, z, y),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (y, x, -z),
    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (-z, -y, -x)
]

template = [k(1, 2, 3) for k in lambdas]

products = {
    (a, b): template.index(lambdas[a](*lambdas[b](1, 2, 3))) for a in range(24) for b in range(24)
}

inverses = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 8,
    8: 4,
    5: 11,
    11: 5,
    6: 9,
    9: 6,
    7: 10,
    10: 7,
    15: 15,
    12: 13,
    13: 12,
    14: 14,
    16: 16,
    17: 18,
    18: 17,
    19: 19,
    20: 22,
    21: 21,
    23: 23,
    22: 20
}

def subt(t1, t2):
    return tuple(x-y for x, y in zip(t1, t2))

def subfield(field, pt):
    return [subt(x, pt) for x in field]

def all_transformations(field):
    arr = []
    for l in lambdas:
        arr.append([l(*t) for t in field])
    return arr

def max_matching(field1, field2):
    maxmatch = 0
    data = None
    for p, transform in enumerate(all_transformations(field1)):
        for i in range(len(field1)):
            for j in range(len(field2)):
                if i == j: continue
                f1 = subfield(transform, transform[i])
                f2 = subfield(field2, field2[j])
                new = sum(k in f2 for k in f1)
                if new > maxmatch:
                    maxmatch = new
                    # if maxmatch >= 12: print(p, i, j)
                    data = (i, j, p, subt(field2[j], transform[i]))
    return maxmatch, data

pos = {0: ((0, 0, 0), 0)}
queue = [0]
while len(queue) > 0:
    a = queue.pop(0)
    loc, trans = pos[a]  # transform to get (a) back to origin
    for b in range(AMT):
        print(a, b)
        if a == b: continue
        maxmatch, data = max_matching(scanners[a], scanners[b])
        if data is None: continue
        _, _, newtrans, offset = data
        actualnewtrans = products[trans, inverses[newtrans]]
        if maxmatch >= 12:
            if b not in pos:
                queue.append(b)
                pos[b] = (tuple(loc[n] - lambdas[actualnewtrans](*offset)[n] for n in range(3)), actualnewtrans)

beacons = set()
for a, (loc, trans) in pos.items():
    func = lambdas[trans]
    for n in scanners[a]:
        transposed = func(*n)
        beacons.add(tuple(loc[i] + transposed[i] for i in range(3)))
print(len(beacons))
maxman = 0
for _, (loc1, _) in pos.items():
    for _, (loc2, _) in pos.items():
        if loc1 == loc2: continue
        x1, y1, z1 = loc1
        x2, y2, z2 = loc2
        man = abs(x2-x1) + abs(y2-y1) + abs(z2-z1)
        if man > maxman:
            maxman = man
print(maxman)