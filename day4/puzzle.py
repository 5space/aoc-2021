with open("input.txt", "r") as file:
    lines = file.read().split("\n\n")

start, lines = lines[0], lines[1:]

nums = list(map(int, start.split(",")))

boards = [[list(map(int, filter(lambda x: x not in ("", "\n"), line.split(" ")))) for line in board.split("\n")] for board in lines]

def is_solved(board, arr):
    pos = [[board[y][x] in arr for x in range(5)] for y in range(5)]
    if any(False not in pos[i] for i in range(5)):
        return True
    elif any(all(pos[y][x] for y in range(5)) for x in range(5)):
        return True
    return False

def loop():
    index = -1
    for i in range(len(nums)):
        solved = [is_solved(board, nums[:i]) for board in boards]
        if solved.count(False) == 1:
            index = solved.index(False)
        if index != -1 and solved[index]:
            board = boards[index]
            print(nums[i-1] * sum(board[y][x] for y in range(5) for x in range(5) if board[y][x] not in nums[:i]))
            return
loop()