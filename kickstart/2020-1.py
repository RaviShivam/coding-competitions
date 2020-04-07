def case():
    N, B = list(map(int, input().split(' ')))
    houses = list(map(int, input().split(' ')))
    houses = sorted(houses)
    c = 0
    ans = 0
    for h in houses:
        if c + h > B:
            break
        c += h
        ans += 1
    return ans


for i in range(int(input())):
    print('Case #{}: {}'.format(i+1, case()))
