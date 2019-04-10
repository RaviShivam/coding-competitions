def run_test():
    _ = input()
    inp = [int(x) for x in input().split(' ')]
    uneven = sorted([inp[x] for x in range(0, len(inp), 2)])
    even = sorted([inp[x] for x in range(1, len(inp), 2)])
    new = []
    while even and uneven:
        new.append(uneven.pop(0))
        new.append(even.pop(0))
    if uneven: new.append(uneven.pop(0))
    if even: new.append(even.pop(0))

    for i in range(len(new)-1):
        if new[i] > new[i+1]: return i
    return 'OK'
    
for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, run_test()))