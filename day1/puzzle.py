with open("input.txt", "r") as file:
    arr = list(map(int, file.read().splitlines()))

print(sum(1 for i in range(1, len(arr)) if arr[i] > arr[i-1]))
print(sum(1 for i in range(3, len(arr)) if arr[i] > arr[i-3]))