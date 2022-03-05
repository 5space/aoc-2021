from collections import defaultdict

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

grid = defaultdict(int)
for line in lines:
    p1, p2 = line.split(" -> ")
    x1, y1 = map(int, p1.split(","))
    x2, y2 = map(int, p2.split(","))
    if x1 == x2:
        y1, y2 = sorted([y1, y2])
        for y in range(y1, y2+1):
            grid[x1, y] += 1
    elif y1 == y2:
        x1, x2 = sorted([x1, x2])
        for x in range(x1, x2+1):
            grid[x, y1] += 1

print(len(grid.values())-list(grid.values()).count(1))

sign = lambda x: 1 if x > 0 else (0 if x == 0 else -1)

grid = defaultdict(int)
for line in lines:
    p1, p2 = line.split(" -> ")
    x1, y1 = map(int, p1.split(","))
    x2, y2 = map(int, p2.split(","))
    dx = sign(x2-x1)
    dy = sign(y2-y1)
    dist = max(abs(x2-x1), abs(y2-y1))
    for n in range(dist + 1):
        grid[x1+dx*n, y1+dy*n] += 1

print(len(grid.values())-list(grid.values()).count(1))