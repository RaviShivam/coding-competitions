def run_test():
    n = int(input())
    opp = input()
    m = {'S': 'E', 'E':'S'}
    mymoves = ''.join([m[x] for x in opp])
    return mymoves
        
for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, run_test()))