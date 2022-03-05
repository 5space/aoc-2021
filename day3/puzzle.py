with open("input.txt", "r") as file:
    lines = file.read().splitlines()

size = len(lines[0])

def elim(arr, i):
    p = [a[i] for a in arr]
    req = "1" if p.count("1") >= p.count("0") else "0"
    return [n for n in arr if n[i] == req]

def elim2(arr, i):
    p = [a[i] for a in arr]
    req = "1" if p.count("1") >= p.count("0") else "0"
    return [n for n in arr if n[i] != req]

arr = lines
i = 0
while len(arr) > 1:
    arr = elim(arr, i)
    i += 1
v1 = arr[0]
arr = lines
i = 0
while len(arr) > 1:
    arr = elim2(arr, i)
    i += 1
v2 = arr[0]

print(int(v1, 2) * int(v2, 2))