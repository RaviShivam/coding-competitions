from itertools import permutations

def run_test():
    N = int(input())
    stones = []
    for _ in range(N):
        S, E, L = map(int, input().split(' '))
        stones.append((S, E, L))

    if len(stones) > 50:
        return run_long(stones)
        
    m = -1
    for eatstones in permutations(stones):
        currtime = 0
        currener = 0

        for S, E, L in eatstones:
            gain = E - currtime*L
            if gain <= 0: break
            currener = currener + gain
            currtime += S
        m = currener if m<currener else m
    return m

def run_long(stones):
    eatstones = sorted(stones, key=lambda tup: (-tup[1], tup[2]), reverse=False)
    currtime = 0
    currener = 0

    for s, e, l in eatstones:
        currener = currener + max(0, e - (currtime*l))
        currtime += s
    return currener

for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, run_test()))