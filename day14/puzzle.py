from collections import defaultdict

with open("input.txt", "r") as file:
    code, lines = file.read().split("\n\n")

inst = {}

for line in lines.split("\n"):
    k, v = line.split(" -> ")
    inst[k] = v

counts = defaultdict(int)
amts = defaultdict(int)
for i in range(len(code)-1):
    counts[code[i:i+2]] += 1
for n in code:
    amts[n] += 1

def iterate():
    global counts
    new = counts.copy()
    for k, v in counts.items():
        a, b = list(k)
        n = inst[k]
        new[a+n] += v
        new[n+b] += v
        new[a+b] -= v
        amts[n] += v
    counts = new

for _ in range(10): iterate()
print(max(amts.values()) - min(amts.values()))
for _ in range(30): iterate()
print(max(amts.values()) - min(amts.values()))
print(counts)