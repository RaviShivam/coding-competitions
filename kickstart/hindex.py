import numpy as np 

def run_test():
    n = int(input())
    A = list((map(int, input().split(' '))))
    newA = []
    p = []
    pasth = 0
    for i in range(1, n+1):
        newA.append(A[i-1])
        newA = list(filter(lambda x: x>pasth, newA))
        h = max(pasth, len(newA))
        p.append(h)
        pasth = h
    return ' '.join(map(str, p))

for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, run_test()))