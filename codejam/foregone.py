from random import randint

def run_test1():
    n = input()
    substr = sum([10**i for i, e in enumerate(n[::-1]) if e=='4'])
    return "{} {}".format(substr, int(n)-substr)
    
def run_test():
    n = int(input())
    if '4' not in str(n):
        return "{} {}".format(0, n)

    while True:
        a = randint(1, n)
        b = n - a
        if '4' not in str(a) and '4' not in str(b):
            return "{} {}".format(a, b)


for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, run_test1()))