with open("input.txt", "r") as file:
    lines = file.read().splitlines()

matrix = [list(map(int, list(line))) for line in lines]
SIZE = len(matrix)

def up(arr, n):
    return [1+(e+n-1)%9 for e in arr]

for k in range(1, 5):
    for i in range(SIZE):
        matrix.append(up(matrix[i], k))
for i in range(len(matrix)):
    l = matrix[i].copy()
    for k in range(1, 5):
        matrix[i] += up(l, k)
SIZE *= 5

potential = [[float("inf") for _ in range(SIZE)] for _ in range(SIZE)]
potential[0][0] = matrix[0][0]

neighbors = lambda x, y: filter(lambda n: n[0] in range(SIZE) and n[1] in range(SIZE),
                              [(x+1, y), (x-1, y), (x, y+1), (x, y-1)])

last = 0
for i in range(SIZE):
    for y in range(SIZE):
        for x in range(SIZE):
            for (x2, y2) in neighbors(x, y):
                potential[x][y] = min(potential[x][y], potential[x2][y2] + matrix[x][y])
    new = potential[-1][-1] - potential[0][0]
    if new == last:
        print(new)
        break
    last = new