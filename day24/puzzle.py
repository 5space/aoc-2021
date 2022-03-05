def process1(z, w, a, b):
    if z%26 + a == w: return z
    else: return 26*z + w + b

def process2(z, w, a, b):
    if z%26 + a == w: return z//26
    else: return z - z%26 + w + b

instrs = [
    (14, 8),
    (13, 8),
    (13, 3),
    (12, 10),
    (-12, 8),
    (12, 8),
    (-2, 8),
    (-11, 5),
    (13, 9),
    (14, 3),
    (0, 4),
    (-12, 9),
    (-13, 2),  # 
    (-6, 7)  # 0
]
16931171414113
# push i0+8
# push i1+8
# push i2+3
# push i3+10
# pop (i4 = i3+10-12)
# push i5+8
# pop (i6 = i5+8-2)
# pop (i7 = i2+3-11)
# push i8+9
# push i9+3
# pop (i10 = i9+3)
# pop (i11 = i8+9-13)
# pop (i12 = i1+8-13)
# pop (i13 = i0+8-6)

def base26(x):
    chars = "0123456789ABCDEFGHIJKLMNOP"
    s = ""
    while x > 0:
        x, v = divmod(x, 26)
        s = chars[v] + s
    return s

# states = [(0, 0)]  # (z, w)

# for i in range(14):
#     new = []
#     a, b = instrs[i]
#     if i in (0, 1, 2, 3, 5, 8, 9):
#         for z, w_full in states:
#             for w in range(1, 10):
#                 z2 = process1(z, w, a, b)
#                 new.append((z2, 10*w_full + w))
#     else:
#         for z, w_full in states:
#             for w in range(1, 10):
#                 z2 = process2(z, w, a, b)
#                 if z2 < z:
#                     new.append((z2, 10*w_full + w))
#                     break
#     states = new
#     print(len(states))

# print(states)

def test(val):
    z = 0
    for i, char in enumerate(val):
        char = val[i]
        a, b = instrs[i]
        if i in (0, 1, 2, 3, 5, 8, 9):
            z = process1(z, char, a, b)
        else:
            z = process2(z, char, a, b)
        print(str(instrs[i]).ljust(10), val[i], base26(z))
    return z

print(test([7,9,9,9,7,3,9,1,9,6,9,6,4,9]))