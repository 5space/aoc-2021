from math import ceil

with open("input.txt", "r") as file:
    code = file.read()

code = bin(int(code, 16))[2:]
code = code.zfill(4*ceil(len(code)/4))

def pop(k):
    global code
    n, code = code[:k], code[k:]
    return int(n, 2)

def prod(arr):
    t = 1
    for s in arr: t *= s
    return t

total = 0
def read_packet():
    global code, total
    version = pop(3)
    type_ = pop(3)
    total += version
    if type_ == 4:
        number = 0
        while True:
            if pop(1) == 1:
                number = (number << 4) + pop(4)
            else:
                number = (number << 4) + pop(4)
                return number
    else:
        typeid = pop(1)
        subs = []
        if typeid == 0:
            bitlength = pop(15)
            curr = len(code)
            while len(code) > curr-bitlength:
                subs.append(read_packet())
        else:
            subpackets = pop(11)
            for _ in range(subpackets):
                subs.append(read_packet())
        
        if type_ == 0: return sum(subs)
        elif type_ == 1: return prod(subs)
        elif type_ == 2: return min(subs)
        elif type_ == 3: return max(subs)
        elif type_ == 5: return int(subs[0] > subs[1])
        elif type_ == 6: return int(subs[0] < subs[1])
        elif type_ == 7: return int(subs[0] == subs[1])
    return 0

result = read_packet()
print(total)
print(result)