with open("input.txt", "r") as file:
    lines = file.read().splitlines()

grid = [list(map(int, list(line))) for line in lines]

total = 0
for _ in range(100):
    flashed = []
    to_flash = 1
    for x in range(10):
        for y in range(10):
            grid[x][y] += 1
    while to_flash > 0:
        to_flash = 0
        for x in range(10):
            for y in range(10):
                if (x, y) in flashed: continue
                if grid[x][y] > 9:
                    grid[x][y] = 0
                    for (x2, y2) in [(x+1, y), (x, y+1), (x-1, y), (x, y-1), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]:
                        if x2 not in range(10) or y2 not in range(10): continue
                        grid[x2][y2] += 1
                    flashed.append((x, y))
                    total += 1
                    to_flash += 1
    for x, y in flashed:
        grid[x][y] = 0
print(total)

grid = [list(map(int, list(line))) for line in lines]

for i in range(1, 1000001):
    flashed = []
    to_flash = 1
    for x in range(10):
        for y in range(10):
            grid[x][y] += 1
    while to_flash > 0:
        to_flash = 0
        for x in range(10):
            for y in range(10):
                if (x, y) in flashed: continue
                if grid[x][y] > 9:
                    grid[x][y] = 0
                    for (x2, y2) in [(x+1, y), (x, y+1), (x-1, y), (x, y-1), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]:
                        if x2 not in range(10) or y2 not in range(10): continue
                        grid[x2][y2] += 1
                    flashed.append((x, y))
                    to_flash += 1
    if len(flashed) == 100:
        break
    for x, y in flashed:
        grid[x][y] = 0
print(i)