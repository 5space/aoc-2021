with open("input.txt", "r") as file:
    lines = file.read().splitlines()

import sys
sys.setrecursionlimit(20000000)

# start = ".......CDCABBDA"
start = ".......BACDBCDA"
end = ".......AABBCCDD"

def slide(s, i1, i2):
    c1, c2 = s[i2], s[i1]
    if i1 < i2: return s[:i1] + c1 + s[i1+1:i2] + c2 + s[i2+1:]
    else: return s[:i2] + c2 + s[i2+1:i1] + c1 + s[i1+1:]

def is_legal(s, i1, i2):
    if s[i1] == ".": return False
    id = "ABCD".index(s[i1])
    if i2 >= 7 and id != (i2-7)//2: return False
    if any(s[i3] != "." for i3 in in_way[i1, i2]): return False
    if i2 >= 7 and i2 % 2 == 1 and s[i2+1] in "ABCD" and s[i2+1] != s[i1]: return False
    if i2 >= 7 and i2 % 2 == 1 and s[i2+1] == ".": return False
    return True

distmap = [(0, 0), (1, 0), (3, 0), (5, 0), (7, 0), (9, 0), (10, 0), (2, 1), (2, 2), (4, 1), (4, 2), (6, 1), (6, 2), (8, 1), (8, 2)]

import networkx as nx

G = nx.Graph()
G.add_nodes_from(range(15))
G.add_edges_from(
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (1, 7), (2, 7), (7, 8), (2, 9), (3, 9), (9, 10), (3, 11), (4, 11), (11, 12), (4, 13), (5, 13), (13, 14)]
)

in_way = {}
for i1 in range(15):
    for i2 in range(15):
        if i1 == i2: continue
        in_way[i1, i2] = nx.shortest_path(G, i1, i2)[1:-1]

def dist(i1, i2):
    x1, y1 = distmap[i1]
    x2, y2 = distmap[i2]
    return abs(x2-x1) + abs(y2-y1)

def disp(state):
    print()
    print("#############")
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o = state
    print(f"#{a}{b}.{c}.{d}.{e}.{f}{g}#")
    print(f"  #{h}#{j}#{l}#{n}#  ")
    print(f"  #{i}#{k}#{m}#{o}#  ")

memory = {end: 0}
process = set()
def min_cost(state):
    disp(state)
    if state == end: return 0
    if state in memory: return memory[state]
    process.add(state)
    valid_moves = []
    for i1 in range(15):
        if state[i1] == ".": continue
        size = 10**("ABCD".index(state[i1]))
        for i2 in range(15):
            if i2 == i1 or state[i2] != ".": continue
            if is_legal(state, i1, i2):
                s = slide(state, i1, i2)
                if s not in process:
                    valid_moves.append((size*dist(i1, i2), s))
    if len(valid_moves) == 0:
        memory[state] = 10000000000000
        return memory[state]  # not feasible
    memory[state] = min(c + min_cost(s) for c, s in valid_moves)
    process.remove(state)
    return memory[state]

print(min_cost(start))
print(memory)