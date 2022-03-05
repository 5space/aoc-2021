with open("input.txt", "r") as file:
    lines = file.read().splitlines()

grid = [[".>v".index(c) for c in line] for line in lines]

SIZEX = len(grid[0])
SIZEY = len(grid)

steps = 0
old = []
while old != grid:
    old = grid
    new = [line[:] for line in grid]
    for y in range(SIZEY):
        for x in range(SIZEX):
            x2 = (x+1)%SIZEX
            if grid[y][x] == 1 and grid[y][x2] == 0:
                new[y][x] = 0
                new[y][x2] = 1
    grid = new
    new = [line[:] for line in grid]
    for y in range(SIZEY):
        y2 = (y+1)%SIZEY
        for x in range(SIZEX):
            if grid[y][x] == 2 and grid[y2][x] == 0:
                new[y][x] = 0
                new[y2][x] = 2
    grid = new
    steps += 1

print(steps)