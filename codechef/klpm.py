from itertools import permutations
txt = input()
for p in permutations(txt):
    print(p)