from itertools import accumulate
import numpy as np

def knapSack(W , wt , val , n): 
    if n == 0 or W == 0 : 
        return 0
    if (wt[n-1] > W): 
        return knapSack(W , wt , val , n-1) 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), 
                   knapSack(W , wt , val , n-1)) 

def case():
    N, K, P = list(map(int, input().split(" ")))
    stacks = [list(accumulate(list(map(int, input().split(" "))))) for _ in range(N)]
    wt, vals = [], []
    for s in stacks:
        for i, v in enumerate(s):
            wt.append(i+1)
            vals.append(v)
    return knapSack(P, wt, vals, len(vals)-1)

  

for i in range(int(input())):
    print("Case #{}: {}".format(i+1, case()))