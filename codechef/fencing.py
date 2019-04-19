import numpy as np
def fence(mat):
    if int(np.sum(mat)) == 0:
        return 0
    if mat.shape==(1,1):
        return 4
    x, y = mat.shape
    ax = 0 if x>=y else 1
    ns = y//2 if ax else x//2
    mat1, mat2 = np.split(mat, [ns], axis=ax)
    v1, v2 = fence(mat1), fence(mat2)
    if ax:
        rmv = np.sum(np.multiply(mat1[:, -1], mat2[:, 0]))
    else:
        rmv = np.sum(np.multiply(mat1[-1, :], mat2[0, :]))
    return v1+v2-2*rmv

def divideconquer():
    n, m, k = map(int, input().split(' '))
    mat = np.zeros((n, m))
    for _ in range(k):
        mat[tuple(map(lambda x: int(x)-1, input().split()))] = 1
    print(int(fence(mat)))


neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]] 
def testcase():
    n, m, k = map(int, input().split(' '))
    totfences = k*4
    ap = set()
    for _ in range(k):
        ap.add(tuple(map(int, input().split(' '))))
    for p in ap:
        rmv = sum([1 for adj in neighbors if (p[0]+adj[0], p[1]+adj[1]) in ap])
        totfences -= rmv
    print(totfences)
    
for i in range(int(input())):
    testcase()