with open("input.txt", "r") as file:
    lines = file.read().splitlines()

def split(tree):
    for i, (n, loc) in enumerate(tree):
        if n >= 10:
            L, R = n//2, n - n//2
            tree[i] = [L, loc + "L"]
            tree.insert(i+1, [R, loc + "R"])
            return True
    return False

def explode(tree):
    for i, (n1, loc1) in enumerate(tree[:-1]):
        n2, loc2 = tree[i+1]
        if loc1.endswith("L") and len(loc1) == len(loc2) > 4:
            if i > 0: tree[i-1][0] += n1
            if i < len(tree)-2: tree[i+2][0] += n2
            tree.pop(i+1)
            tree[i] = [0, loc1[:-1]]
            return True
    return False

def reduce(tree):
    while True:
        if not explode(tree):
            if not split(tree):
                break
    return tree

def add(tree1, tree2):
    tree = []
    for n, loc in tree1:
        tree.append([n, "L" + loc])
    for n, loc in tree2:
        tree.append([n, "R" + loc])
    return tree

def to_tree(arr):
    tree = []
    loc = ""
    for n in arr:
        if n == "[": loc += "L"
        elif n == ",": loc = loc[:-1] + "R"
        elif n == "]": loc = loc[:-1]
        else: tree.append([int(n), loc])
    return tree

def magnitude(tree):
    total = 0
    for n, loc in tree:
        L = loc.count("L")
        R = loc.count("R")
        total += (3**L * 2**R) * n
    return total

combined = reduce(to_tree(lines.pop(0)))
for line in lines:
    tree = to_tree(line)
    combined = reduce(add(combined, tree))
print(magnitude(combined))