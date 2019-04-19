def brute_force():
    n = int(input())
    s, c = input().split(' ')
    counts = 0
    for window in range(n):
        # l = [x for x in [s[j:j+window+1] for j in range(n-window)] if c in x]
        # counts += len(l)
        for j in range(n - window):
            substr = s[j:j+window+1]
            if c in substr:
                counts += 1
    
    print(counts)

def test_case():
    n = int(input())
    s, c = input().split(' ')
    locs = [i for i, e in enumerate(s) if s[i] == c]
    tokens = set()
    for window in range(1, n+1):
        for loc in locs:
            start, end = max(loc-(window-1), 0), min(n, loc+1)
            # print('start, end: {}, {}'.format(start, end))
            for j in range(start, end):
                substr = s[j: min(j+window, n)]
                # print('substr = {}, {}, {}'.format(substr, j, min(j+window, n)))
                if c in substr:
                    tokens.add((j, min(j+window, n)))
        # print('tokens found: {}'.format(len(tokens)))
    print(len(tokens))

def test_case2():
    n = int(input())
    s, c = input().split(' ')
    locs = [i for i, e in enumerate(s) if s[i] == c]
    tokens = set()
    for l in locs:
        tokens.add((l, l+1))
        a, b = range(l), range(l+2, n+1)
        tokens |= set(zip(a, [l+1]*l))
        tokens |= set(zip([l]*(n-l-1), b))
        [tokens.update(set(zip([x]*len(b), b))) for x in a]
    # print(tokens)
    print(len(tokens))

def solve():
    n = int(input())
    s, c = input().split(' ')
    locs = [i for i, e in enumerate(s) if s[i] == c]
    counts, lstl = 0, -1
    for l in locs:
        f, b = (l-(lstl+1)), (n-l-1)
        # print(f, b)
        counts += 1+f+b+f*b
        lstl = l
    print(counts)


for j in range(int(input())):
    solve()
    # break
    # brute_force()
    # test_case()