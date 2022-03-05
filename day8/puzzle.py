with open("input.txt", "r") as file:
    lines = [[(k := line.split(" | "))[0].split(" "), k[1].split(" ")] for line in file.read().splitlines()]

total = 0
for a1, a2 in lines:
    for n in a2:
        if len(n) in (2, 4, 3, 7):
            total += 1
print(total)

from itertools import permutations

digits = [0b1110111, 0b0100100, 0b1011101, 0b1101101, 0b0101110, 0b1101011, 0b1111011, 0b0100101, 0b1111111, 0b1101111]

def get_combo(gibberish):
    for perm in permutations("abcdefg"):
        flag = True
        for code in gibberish:
            binary = sum(1 << i for i in range(7) if perm[i] in code)
            if binary not in digits:
                flag = False
        if flag:
            return perm

total = 0
for a1, a2 in lines:
    perm = get_combo(a1)
    value = [digits.index(sum(1 << perm.index(c) for c in w)) for w in a2]
    p = int("".join(map(str, value)))
    total += p
print(total)

for a1, a2 in lines:
    codes = [set(x) for x in a1]
    solution = [None for _ in range(10)]