m = 1000000007

prevmax = (1, 1)

def run_test(N):
    global prevmax
    a, b = prevmax[1], prevmax[0]+1
    for _ in range(b-1, N):
        a = (a + b + a*b)%m
        b = b + 1 
    prevmax = (b-1, a)
    return a

original = [int(input()) for _ in range(int(input()))]
tests = sorted(original)
h = {}
for t in tests:
    h[t] = run_test(t)
for o in original:
    print(h[o])