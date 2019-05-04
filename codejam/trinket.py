from collections import Counter

def run_test():
    N, S = map(int, input().split(' '))
    l = list(map(int, input().split(' ')))
    mbring = -1
    for wz in range(S+1, N+1):
        for s in range(0, N-wz+1):
            c = Counter(l[s:s+wz])
            bring = 0
            for v in dict(c).values():
                if v <= S:
                    bring += v
            mbring = bring if bring > mbring else mbring
    return mbring
    

for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, run_test()))