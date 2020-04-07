import sys 

def complement(arr):
    for i, x in enumerate(arr):
        if (arr[i] is not None):
            arr[i] = int(not x)
    return arr

def solve(t, B):
    switch = 1
    same, diff = None, None
    same_val, diff_val = None, None
    b = [None]*B
    for round in range(15):
        if None not in b: break
        counts = 0
        if bool(same) and not bool(diff): 
            print(same)
            temp_same_val = int(input())
            b = complement(b) if temp_same_val != same_val else b
            same_val = temp_same_val
            counts += 1

        if bool(diff) and not bool(same): 
            print(diff)
            temp_diff_val = int(input())
            b = complement(b) if temp_diff_val != diff_val else b
            diff_val = temp_diff_val
            counts += 1
        
        if bool(diff) and bool(same):
            print(same)
            temp_same_val = int(input())

            print(diff)
            temp_diff_val = int(input())
            
            same_check, diff_check = temp_same_val == same_val, temp_diff_val == diff_val
            if not(same_check) and not(diff_check):
                b = complement(b)
            if same_check and not diff_check:
                b = list(reversed(b))
            if not same_check and diff_check:
                b = complement(list(reversed(b)))
            same_val, diff_val = temp_same_val, temp_diff_val
            counts += 2

        if counts == 1:
            print(B)
            _ = input()
            counts += 1

        for qry in range(10 - counts):
            if None not in b: break
            switch = (switch+1)%2
            cursor = B - b[::-1].index(None) if switch == 1 else b.index(None) + 1 # 1-indexed
            print(cursor)
            response = int(input())
            b[cursor - 1] = response

            opp_cursor = B - (cursor - 1) # 1-indexed
            if same is None and (b[cursor - 1] == b[opp_cursor - 1]):
                same, same_val = cursor, b[cursor - 1]

            if diff is None and (b[cursor - 1] != b[opp_cursor - 1]) and None not in [b[cursor - 1], b[opp_cursor - 1]]:
                diff, diff_val = cursor, b[cursor - 1]

    print(''.join(map(str, b)))
    print('[Case #{0}] Response from Judge System: {1}'.format(t, input()), file=sys.stderr)

if __name__ == "__main__":
    T, B = map(int, input().split(' '))
    print('# of test cases: {}, Value of B: {}'.format(T, B), file=sys.stderr)
    for t in range(1, T + 1):
        solve(t, B)