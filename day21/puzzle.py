from collections import defaultdict

universes = {(0, 0, 7, 6): 1}
p1_wins = 0
p2_wins = 0

probs = [0, 0, 1, 3, 6, 7, 6, 3, 1]

while len(universes) > 0:
    print(len(universes))
    new = defaultdict(int)
    for (s1, s2, p1, p2), n in universes.items():
        for i in range(2, 9):
            new[s1+(p1+i)%10+1, s2, (p1+i)%10+1, p2] += probs[i]*n
    for k, v in new.copy().items():
        if k[0] >= 100:
            p1_wins += v
            new.pop(k)
    universes = new
    print(len(universes))
    
    new = defaultdict(int)
    for (s1, s2, p1, p2), n in universes.items():
        for i in range(2, 9):
            new[s1, s2+(p2+i)%10+1, p1, (p2+i)%10+1] += probs[i]*n
    for k, v in new.copy().items():
        if k[1] >= 100:
            p2_wins += v
            new.pop(k)
    universes = new

print(p1_wins, p2_wins)