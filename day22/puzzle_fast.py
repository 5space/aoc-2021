with open("input.txt", "r") as file:
    lines = file.read().splitlines()

import time
start = time.time()

instrs = []
for line in lines:
    onoff, rest = line.split(" ")
    onoff = onoff == "on"
    x, y, z = rest.split(",")
    minx, maxx = x[2:].split("..")
    miny, maxy = y[2:].split("..")
    minz, maxz = z[2:].split("..")
    instrs.append((onoff, int(minx), int(miny), int(minz), int(maxx)+1, int(maxy)+1, int(maxz)+1))

lessthan = lambda n: n[0] < n[1]

class AABB:
    
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1, self.x2 = x1, x2
        self.y1, self.y2 = y1, y2
        self.z1, self.z2 = z1, z2
    
    def vol(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1) * (self.z2 - self.z1)
    
    def intersect(self, other):
        x3 = max(self.x1, other.x1)
        y3 = max(self.y1, other.y1)
        z3 = max(self.z1, other.z1)
        x4 = min(self.x2, other.x2)
        y4 = min(self.y2, other.y2)
        z4 = min(self.z2, other.z2)
        if x3<x4 and y3<y4 and z3<z4: return AABB(x3, y3, z3, x4, y4, z4)
        else: return None

    def split(self, other):
        inter = self.intersect(other)
        xinter = [(self.x1, inter.x1), (inter.x1, inter.x2), (inter.x2, self.x2)]
        yinter = [(self.y1, inter.y1), (inter.y1, inter.y2), (inter.y2, self.y2)]
        zinter = [(self.z1, inter.z1), (inter.z1, inter.z2), (inter.z2, self.z2)]
        result = []
        for x1, x2 in filter(lessthan, xinter):
            for y1, y2 in filter(lessthan, yinter):
                for z1, z2 in filter(lessthan, zinter):
                    if (x1, x2) != (inter.x1, inter.x2) or (y1, y2) != (inter.y1, inter.y2) or (z1, z2) != (inter.z1, inter.z2):
                        result.append(AABB(x1, y1, z1, x2, y2, z2))
        return result

cuboids = []
for onoff, x1, y1, z1, x2, y2, z2 in instrs:
    newcuboid = AABB(x1, y1, z1, x2, y2, z2)
    newlist = []
    for cuboid in cuboids:
        if cuboid.intersect(newcuboid):
            newlist += cuboid.split(newcuboid)
        else:
            newlist.append(cuboid)
    if onoff:
        newlist.append(newcuboid)
    cuboids = newlist

print(sum(c.vol() for c in cuboids))
print(time.time() - start)