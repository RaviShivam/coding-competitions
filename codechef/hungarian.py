import numpy as np
def run_test():
    N = int(input())
    M = np.zeros((N, N))
    for n in range(N):
        M[n,:] = np.array(list(map(int, input().split(' '))))
    for r in range(M.shape[0]):
        if 0 not in M[r, :]:
            return 'NO'
    for c in range(M.shape[1]):
        if 0 not in M[:, c]:
            return 'NO'
    return 'YES'
for _ in range(int(input())):
    print(run_test())