minx = 150
maxx = 193
miny = -136
maxy = -86

def goes_in(vx, vy):
    px, py = 0, 0
    while py >= miny:
        px += vx
        py += vy
        if vx > 0: vx -= 1
        elif vx < 0: vx += 1
        vy -= 1
        if minx <= px <= maxx and miny <= py <= maxy:
            return True
    return False

total = 0
for x in range(1, maxx+1):
    for y in range(miny, 136):  # max y value from part 1
        if goes_in(x, y):
            total += 1
print(total)

