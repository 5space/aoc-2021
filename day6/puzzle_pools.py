with open("input.txt", "r") as file:
    nums = list(map(int, file.read().split(",")))

# pools[i] = number of fish with age i
pools = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for num in nums:
    pools[num] += 1

for _ in range(80):
    newpools = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(9):
        if i == 0:
            newpools[6] += pools[i]
            newpools[8] += pools[i]
        else:
            newpools[i-1] += pools[i]
    pools = newpools

print(sum(pools))