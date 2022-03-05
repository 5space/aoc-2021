with open("input.txt", "r") as file:
    lines = [list(map(int, list(k))) for k in file.read().splitlines()]

total = 0
points = []
for x in range(len(lines)):
    for y in range(len(lines[0])):
        flag = True
        for (x2, y2) in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
            if x2 not in range(len(lines)) or y2 not in range(len(lines[0])): continue
            if lines[x2][y2] <= lines[x][y]: flag = False
        if flag:
            points.append((x, y))
            total += 1 + lines[x][y]
print(total)

sizes = []
for x0, y0 in points:
    basin = [(x0, y0)]
    queue = [(x0, y0)]
    while len(queue) > 0:
        x, y = queue.pop(0)
        for (x2, y2) in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
            if x2 not in range(len(lines)) or y2 not in range(len(lines[0])): continue
            if (x2, y2) in basin or lines[x2][y2] == 9: continue
            basin.append((x2, y2))
            queue.append((x2, y2))
    sizes.append(len(basin))
sizes.sort()
print(sizes[-3]*sizes[-2]*sizes[-1])