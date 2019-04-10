from random import randint

cases = int(input())

def run_test():
    a, b = map(int, input().split(' '))
    c, n = 0, int(input())
    while c <= n:
        g = randint(a, b)
        print(g)
        state = input()
        if state == 'TOO_SMALL':
            a = c
        if state == 'TOO_BIG':
            b = c
        if state == 'CORRECT':
            return
        c += 1

for c in range(cases):
    run_test()
