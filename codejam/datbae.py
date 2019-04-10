import sys
import math

log_file = open('debug', 'w')

def debug(*args):
    log_file.write("DEBUGGER LOG: {}".format(' '.join(map(str, args))) + '\n')

def printG(*args):
    print(' '.join(map(str, args)))
    sys.stdout.flush()
    log_file.write("SENDING TO JUDGE: {}".format(' '.join(map(str, args))) + '\n')
    log_file.flush()

def run_test():
    N, B, F = list(map(int, input().split(' ')))
    cols = []
    num_bits = min(math.ceil(math.log(N, 2)), F)
    max_val = 2**num_bits 
    [cols.append(list(format(i%max_val, 'b').zfill(F))) for i in range(N)]
    cols = list(map(list, zip(*cols)))
    responses = []
    for i in range(F):
        print(''.join(cols[i]))
        responses.append(input())
    working = [int(''.join(x), 2) for x in list(zip(*list(map(list, responses))))]
    curr, broken = 0, []
    for i in range(N):
        if curr == len(working): 
            [broken.append(j) for j in range(i, N)]
            break
        if working[curr] != i%max_val:
            broken.append(i)
        else:
            curr += 1
    broken = ' '.join(map(str, broken))
    print(broken)
    input()

ts = int(input())
for i in range(1, ts + 1):
    run_test()