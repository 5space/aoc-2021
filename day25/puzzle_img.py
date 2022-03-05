with open("input.txt", "r") as file:
    lines = file.read().splitlines()

import time
start = time.perf_counter()

grid = [[".>v".index(c) for c in line] for line in lines]

SIZEX = len(grid[0])
SIZEY = len(grid)

import imageio
from PIL import Image

def img_from_grid(grid):
    img = Image.new("RGB", (SIZEX, SIZEY), (0, 0, 0))
    pixels = img.load()
    for y in range(SIZEY):
        for x in range(SIZEX):
            if grid[y][x] == 1:
                pixels[x, y] = (255, 0, 0)
            elif grid[y][x] == 2:
                pixels[x, y] = (0, 255, 0)
    return img

steps = 0
old = []
img_from_grid(grid).save("frame.png")
images = [imageio.imread("frame.png")] * 20
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
    img_from_grid(grid).save("frame.png")
    images.append(imageio.imread("frame.png"))
    new = [line[:] for line in grid]
    for y in range(SIZEY):
        y2 = (y+1)%SIZEY
        for x in range(SIZEX):
            if grid[y][x] == 2 and grid[y2][x] == 0:
                new[y][x] = 0
                new[y2][x] = 2
    grid = new
    img_from_grid(grid).save("frame.png")
    images.append(imageio.imread("frame.png"))
    steps += 1
    print(steps)
images += [imageio.imread("frame.png")] * 20

imageio.mimsave("movie.gif", images, format="GIF", fps=30)