#! /home/ravishivam/miniconda3/bin/python
import sys

def looper(B=20):
    checker1 = []
    checker2 = []
    for i in range(15):
        print(1)
        response = int(input())
        checker1.append(response)
        print(2)
        response = int(input())
        checker1.append(response)
        print(3)
        response = int(input())
        checker1.append(response)
        print(4)
        response = int(input())
        checker1.append(response)
        print(5)
        response = int(input())
        checker1.append(response)
        print(B)
        response = int(input())
        checker2.append(response)
        print(B-1)
        response = int(input())
        checker2.append(response)
        print(B-2)
        response = int(input())
        checker2.append(response)
        print(B-3)
        response = int(input())
        checker2.append(response)
        print(20)
        response = int(input())
        checker2.append(response)
        print("[Round {}] ".format(i), checker1, checker2, file=sys.stderr)
        checker1 = []
        checker2 = []

def test_case1(T, B=10):
    b = []
    for i in range(B):
        request_i = (i%B)+1
        # print('[{}] Requesting bit at position: {}'.format(i+1, request_i), file=sys.stderr)
        print(request_i)
        response = int(input())
        b.append(response)
        # print('[{}] Returned value: {}'.format(i+1, response), file=sys.stderr)
    print(''.join(map(str, b)))
    response = input()
    print("Judge System at T={}: {}".format(T, response), file=sys.stderr)

def complement(arr):
    return [int(not x) if x is not None else None for x in arr]
    
def reverse_complement(arr):
    arr = list(reversed(arr))
    return [int(not x) if x is not None else None for x in arr]

def is_complement(prev_checkbits1, prev_checkbits2, checkbits1, checkbits2):
    prev_checkbits1, prev_checkbits2, checkbits1, checkbits2 = prev_checkbits1.copy(), prev_checkbits2.copy(), checkbits1.copy(), checkbits2.copy()
    check1 = complement(prev_checkbits1) == checkbits1
    prev_checkbits1, prev_checkbits2, checkbits1, checkbits2 = prev_checkbits1.copy(), prev_checkbits2.copy(), checkbits1.copy(), checkbits2.copy()
    check2 = complement(prev_checkbits2) == checkbits2
    prev_checkbits1, prev_checkbits2, checkbits1, checkbits2 = prev_checkbits1.copy(), prev_checkbits2.copy(), checkbits1.copy(), checkbits2.copy()
    check3 = complement(prev_checkbits1 + prev_checkbits2) == checkbits1 + checkbits2
    return bool(check1*check2*check3)

def is_reversed(prev_checkbits1, prev_checkbits2, checkbits1, checkbits2):
    prev_checkbits1, prev_checkbits2, checkbits1, checkbits2 = prev_checkbits1.copy(), prev_checkbits2.copy(), checkbits1.copy(), checkbits2.copy()
    check1 = list(reversed(prev_checkbits2)) == checkbits1
    prev_checkbits1, prev_checkbits2, checkbits1, checkbits2 = prev_checkbits1.copy(), prev_checkbits2.copy(), checkbits1.copy(), checkbits2.copy()
    check2 = list(reversed(prev_checkbits1)) == checkbits2
    prev_checkbits1, prev_checkbits2, checkbits1, checkbits2 = prev_checkbits1.copy(), prev_checkbits2.copy(), checkbits1.copy(), checkbits2.copy()
    check3 = list(reversed(prev_checkbits1 + prev_checkbits2)) == checkbits1 + checkbits2
    return bool(check1*check2*check3)

def is_reversed_complemented(prev_checkbits1, prev_checkbits2, checkbits1, checkbits2):
    print(prev_checkbits1, prev_checkbits2, file=sys.stderr)
    print(checkbits1, checkbits2, file=sys.stderr)

    prev_checkbits1, prev_checkbits2, checkbits1, checkbits2 = prev_checkbits1.copy(), prev_checkbits2.copy(), checkbits1.copy(), checkbits2.copy()
    check1 = reverse_complement(prev_checkbits2) == checkbits1

    print(prev_checkbits1, prev_checkbits2, file=sys.stderr)
    print(checkbits1, checkbits2, file=sys.stderr)

    prev_checkbits1, prev_checkbits2, checkbits1, checkbits2 = prev_checkbits1.copy(), prev_checkbits2.copy(), checkbits1.copy(), checkbits2.copy()
    check2 = reverse_complement(prev_checkbits1) == checkbits2

    print(prev_checkbits1, prev_checkbits2, file=sys.stderr)
    print(checkbits1, checkbits2, file=sys.stderr)

    prev_checkbits1, prev_checkbits2, checkbits1, checkbits2 = prev_checkbits1.copy(), prev_checkbits2.copy(), checkbits1.copy(), checkbits2.copy()
    check3 = reverse_complement(prev_checkbits1 + prev_checkbits2) == checkbits1 + checkbits2

    print(prev_checkbits1, prev_checkbits2, file=sys.stderr)
    print(checkbits1, checkbits2, file=sys.stderr)

    print(check1, check2, check3, file=sys.stderr)
    return bool(check1*check2*check3)

def is_same(prev_checkbits1, prev_checkbits2, checkbits1, checkbits2):
    check1 = prev_checkbits1 == checkbits1
    check2 = prev_checkbits2 == checkbits2
    check3 = prev_checkbits1 + checkbits1 == prev_checkbits2 + checkbits2
    return bool(check1*check2*check3)
    
def test_case3(T, B=20):
    starti, endi = -1, -1
    for round in range(1, 9):
        checkbits1 = []
        checkbits2 = []
        for reset_counter in range(4):
            print(round + reset_counter)
            response = int(input())
            checkbits1.append(response)

            print(B-(round+reset_counter)+1)
            response = int(input())
            checkbits2.append(response)
        check1 = list(reversed(checkbits1+checkbits2)) == checkbits1+checkbits2
        check2 = complement(list(reversed(checkbits1+checkbits2))) == checkbits1+checkbits2
        check3 = complement(checkbits1+checkbits2) == checkbits1+checkbits2
        if check1 or check2 or check3:
            continue
        starti, endi = round, B-round+1
        print("Initial checkpoints: ", checkbits1, checkbits2, starti, endi, file=sys.stderr)
        break

    b = B*[None]
    for i in range(6):
        prev_checkbits1 = checkbits1 
        prev_checkbits2 = checkbits2 
        checkbits1 = []
        checkbits2 = []
        for reset_counter in range(4):
            print(starti + reset_counter)
            checkbits1.append(int(input()))

            print(endi-reset_counter)
            checkbits2.append(int(input()))

        c = is_complement(prev_checkbits1, prev_checkbits2, checkbits1, checkbits2)
        r = is_reversed(prev_checkbits1, prev_checkbits2, checkbits1, checkbits2)
        rc = is_reversed_complemented(prev_checkbits1, prev_checkbits2, checkbits1, checkbits2)
        mod = 'No mods'
        if c:
            b = complement(b)
            mod = 'complemented'
        elif r:
            b = list(reversed(b))
            mod = 'reversed'
        elif rc:
            b = reverse_complement(b)
            mod = 'reversed_complemented'
        else:
            pass
        
        b[starti-1:starti+3] = checkbits1
        b[endi-4:endi] = checkbits2

        for _ in range(2):
            nonei = b.index(None)
            print(nonei+1)
            b[nonei] = int(input())

        print("[Round {}] ".format(((i+1)*10) + 1), "c1: {}".format(checkbits1), "c2: {}".format(checkbits2), b, mod, file=sys.stderr)
        if None not in b:
            break


    print(''.join(map(str, b)))
    response = input()
    print("Judge System at T={}: {}".format(T, response), file=sys.stderr)




T, B = map(int, input().split(' '))
print('# of test cases: {}, Value of B: {}'.format(T, B), file=sys.stderr)
for t in range(1, T + 1):
    if B == 10:
        test_case1(t)
    if B == 20:
        test_case3(t)
    if B == 100:
        test_case3(t, B=100)

def test_case2(T, B=20):
    b = B*[None]
    for i in range(6):
        prev_checkbits1 = checkbits1 if i>0 else None
        prev_checkbits2 = checkbits2 if i>0 else None
        checkbits1 = []
        checkbits2 = []
        for reset_counter in range(1, 8 + 1):
            if 1 <= reset_counter <= 4:
                print(reset_counter)
                response = int(input())
                checkbits1.append(response)
                continue

            if 5 <= reset_counter <= 8:
                print(B-(8-reset_counter))
                response = int(input())
                checkbits2.append(response)
                continue

        mod = 'None'
        if i > 0: 
            s = is_same(prev_checkbits1, prev_checkbits2, checkbits1, checkbits2)
            c = is_complement(prev_checkbits1, prev_checkbits2, checkbits1, checkbits2)
            r = is_reversed(prev_checkbits1, prev_checkbits2, checkbits1, checkbits2)
            rc = is_reversed_complemented(prev_checkbits1, prev_checkbits2, checkbits1, checkbits2)
            if s:
                pass
            elif c:
                b = complement(b)
                mod = 'complemented'
            elif r:
                b = list(reversed(b))
                mod = 'reversed'
            elif rc:
                b = reverse_complement(b)
                mod = 'reversed_complemented'
            else:
                pass

        b[:4] = checkbits1
        b[-4:] = checkbits2

        print(5 + i)
        response1 = int(input())
        b[5 + i - 1] = response1

        print(16 - i)
        response2 = int(input())
        b[16 - i - 1] = response2

        print("[Round {}] ".format(((i+1)*10) + 1), "c1: {}".format(checkbits1), "c2: {}".format(checkbits2), b, mod, file=sys.stderr)


    print(''.join(map(str, b)))
    response = input()
    print("Judge System at T={}: {}".format(T, response), file=sys.stderr)