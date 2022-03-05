with open("input.txt", "r") as file:
    lines = file.read().splitlines()

import re
from math import floor, ceil

def do_reduce(arr):
    lastarr = ""
    while lastarr != arr:
        lastarr = arr
        for match in re.finditer(r"\[\d+,\d+\]", arr):
            start, end = match.start(0), match.end(0)
            left, right = map(int, match.group(0)[1:-1].split(","))
            nested = arr[:start].count("[") - arr[:start].count("]")
            if nested >= 4:
                leftarr = arr[:start]
                matchnum = None
                for matchnum in re.finditer(r"\d+", arr[:start]):
                    pass
                if matchnum is not None:
                    value = int(matchnum.group(0))
                    leftarr = arr[:matchnum.start(0)] + str(value + left) + arr[matchnum.end(0):start]
                rightarr = arr[end:]
                for matchnum in re.finditer(r"\d+", arr[end:]):
                    value = int(matchnum.group(0))
                    rightarr = arr[end:end+matchnum.start(0)] + str(value + right) + arr[end+matchnum.end(0):]
                    break
                arr = (leftarr + "0" + rightarr).replace("[,", "[").replace(",]", "]")
                break
        if arr != lastarr:
            lastarr = ""
            continue
        for match in re.finditer(r"\d{2,}", arr):
            start, end = match.start(0), match.end(0)
            value = int(match.group(0))
            new = f"[{floor(value/2)},{ceil(value/2)}]"
            arr = arr[:start] + new + arr[end:]
            break
    return arr

def magn(arr):
    if type(arr) == int: return arr
    else:
        return 3*magn(arr[0]) + 2*magn(arr[1])

pile = lines[0]
pile = do_reduce(pile)
for line in lines[1:]:
    pile = "[" + pile + "," + line + "]"
    pile = do_reduce(pile)
print(magn(eval(pile)))

maxmag = 0
for line1 in lines:
    for line2 in lines:
        if line1 == line2: continue
        pile = "[" + line1 + "," + line2 + "]"
        mag = magn(eval(do_reduce(pile)))
        if mag > maxmag: maxmag = mag
print(maxmag)