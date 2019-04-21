def run_test():
    words = [input() for _ in range(int(input()))]
    dcs = {}
    for w in words:
        for i in range(1, len(w)+1):
            subw = w[-i:]
            if subw in dcs:
                dcs[subw] = [dcs[subw][0] + 1, dcs[subw][1] + [w]]
            else:
                dcs[subw] = [1, [w]]
    print(dcs)
    pairwords = set()
    for k, v in dcs.items():
        if v[0] == 2:
            [pairwords.add(x) for x in v[1]]
    return len(pairwords)
    

for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, run_test()))
    break
