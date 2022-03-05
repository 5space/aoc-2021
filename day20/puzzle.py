from collections import defaultdict

with open("input.txt", "r") as file:
    code, lines = file.read().split("\n\n")

lines = lines.split("\n")

points = defaultdict(lambda: False)
for y in range(len(lines)):
    for x in range(len(lines[0])):
        points[x, y] = lines[y][x] == "#"

neighbors = lambda x, y: [(x+1, y), (x, y+1), (x-1, y), (x, y-1), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]
background = False

for i in range(50):
    newpoints = defaultdict(lambda: background)
    all_neighbors = set(points.keys())
    for point in points:
        for n in neighbors(*point):
            all_neighbors.add(n)
    for x, y in all_neighbors:
        bits = [points[x-1, y-1],
                points[x, y-1],
                points[x+1, y-1],
                points[x-1, y],
                points[x, y],
                points[x+1, y],
                points[x-1, y+1],
                points[x, y+1],
                points[x+1, y+1]]
        index = sum(bits[8-i] << i for i in range(9))
        newpoints[x, y] = code[index] == "#"
    points = newpoints
    background = not background
    print(i)
    # for y in range(-10, 10):
    #     for x in range(-10, 10):
    #         if points[x, y]:
    #             print("██", end="")
    #         else:
    #             print("  ", end="")
    #     print()
print(sum(points[n] for n in points))