from collections import defaultdict
from copy import copy

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

edges = [set(line.split("-")) for line in lines]

def paths_from(vertex, visited=defaultdict(int)):
    total = 0
    for edge in edges:
        if vertex in edge:
            v1, v2 = edge
            if v2 == vertex: v2 = v1
            if v2 == "start": continue
            if visited[v2] >= 1 and v2 == v2.lower() and (2 in visited.values()): continue
            if v2 == "end":
                total += 1
            else:
                visited2 = copy(visited)
                if v2 == v2.lower():
                    visited2[v2] += 1
                total += paths_from(v2, visited2)
    return total

print(paths_from("start"))