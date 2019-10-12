from functools import reduce

def factorial(x):
    if x==1:
        return 1
    return x*factorial(x-1)

for _ in range(int(input())):
    # print(reduce(lambda i, j: i*j, range(1, int(input())+1)))
    print(factorial(int(input())))