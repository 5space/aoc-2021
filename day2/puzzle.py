with open("input.txt", "r") as file:
    lines = file.read().splitlines()

x = 0
y = 0
for line in lines:
    a, b = line.split(" ")
    b = int(b)
    if a == "forward":
        x += b
    elif a == "up":
        y -= b
    elif a == "down":
        y += b
print(x * y)

print((c:=lambda x:sum(int(a[1])for l in open("input.txt").readlines()if(a:=l.split(" "))[0][0]==x))("f")*(c("d")-c("u")))
lambda s, x, c: {"f":(p:=s[0],d:=s[1],a:=s[2])}