def run_case():
    S_int = list(map(int, input()))
    S  = ["{}{}{}".format(int(x)*"(", x, int(x)*")") for x in S_int]
    for i, e in enumerate(S_int):
        if i == 0: continue
        rmvparen = min(S_int[i-1], S_int[i])
        if rmvparen > 0:
            S[i-1] = S[i-1][:-rmvparen] 
            S[i] = S[i][rmvparen:] 
    return ''.join(S)


if __name__ == "__main__":
    for i in range(1, int(input()) + 1):
        print("Case #{0}: {1}".format(i, run_case()))