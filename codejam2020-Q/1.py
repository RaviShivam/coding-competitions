import numpy as np

def run_case():
    N = int(input())
    k, r, c = 0, 0, 0
    M = []
    for i in range(N):
        row = list(map(int, input().split(' ')))
        M.append(row)
        k += row[i]
    M = np.array(M)
    for i in range(N):
        r += 1 if len(np.unique(M[i, :])) < N else 0
        c += 1 if len(np.unique(M[:, i])) < N else 0
    return ' '.join(map(str, (k, r, c)))

if __name__ == "__main__":
    for i in range(1, int(input()) + 1):
        print("Case #{0}: {1}".format(i, run_case()))