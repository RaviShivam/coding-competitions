num = int(input())
vals = sorted(set(map(int, input().split(' '))))
ans = 0 if len(vals) == 1 else vals[-2]%vals[-1]
print(ans)