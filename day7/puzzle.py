with open("input.txt", "r") as file:
    nums = list(map(int, file.read().split(",")))

maxtotal = 1000000000000000000
for i in range(min(nums), max(nums)+1):
    total = sum(abs(a-i)*(abs(a-i)+1)/2 for a in nums)
    if total < maxtotal:
        maxtotal = total
print(maxtotal)


print("+".join(f"abs(x-{i})" for i in nums))