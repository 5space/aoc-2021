with open("input.txt", "r") as file:
    lines = file.read().splitlines()

key = {"}": "{", "]": "[", ")": "(", ">": "<"}

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

total = 0
incomplete = []
for line in lines:
    stack = []
    flag = False
    for c in line:
        if c in "{[(<":
            stack.append(c)
        else:
            if key[c] != stack[-1]:
                total += scores[c]
                flag = True
                break
            stack.pop()
    if not flag:
        add = 0
        for c in stack[::-1]:
            add *= 5
            add += scores[c]
        incomplete.append(add)
incomplete.sort()
print(total)
print(incomplete[len(incomplete)//2])