from collections import Counter 

def run_test():
    N = int(input())
    a = 'codechef'
    t = 'ce'
    meal = ''
    for _ in range(N):
        meal += input()
    count = Counter(meal)
    total = []
    for c in a:
        total.append(count[c] if c not in t else count[c]//2)
    print(min(total))

for _ in range(int(input())):
    run_test()