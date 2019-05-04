from math import ceil

def test_case():
    N, A, B, X, Y, Z = map(int, input().split(' '))
    C = list(map(int, input().split(' ')))
    dtr = ceil((Z-B)/Y)
    finaldayusers = A + (dtr - 1)*X
    neededusers = Z - finaldayusers
    csort = C
    support = 0
    while True:
        for i, v in enumerate(csort):
        if csort[0] == 0:
            return 'RIP'
        neededusers -= csort[0]
        support += 1
        csort[0] = csort[0]//2
        if neededusers <= 0:
            return support



for _ in range(int(input())):
    print(test_case())