with open("input.txt", "r") as file:
    points, folds = file.read().split("\n\n")

grid = set()
for point in points.split("\n"):
    x, y = point.split(",")
    grid.add((int(x), int(y)))

for fold in folds.split("\n"):
    n1, n2 = fold.split("=")
    n2 = int(n2)
    i = 0 if n1[-1] == "x" else 1
    for g in grid.copy():
        x, y = g
        if g[i] > n2:
            grid.remove(g)
            if i == 0:
                grid.add((2*n2 - x, y))
            else:
                grid.add((x, 2*n2-y))

for y in range(-1, 700):
    for x in range(-1, 400):
        if (x, y) in grid:
            print("██", end="")
        else:
            print("  ", end="")
    print()