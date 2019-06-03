n, k = map(int, input().strip().split())
c = 0
for _ in range(n):
    if int(input()) % k == 0:
        c += 1
print(c)