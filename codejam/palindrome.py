from itertools import permutations
def palindrome(cstring):
    found = False
    char_set = set(cstring) # Lets find unique letters

    d_dict = {}
    for c in char_set:
        d_dict[c] = cstring.count(c) # Keep count of each letter

    odd_l = [e for e in d_dict.values() if e%2 == 1] # Check how many has odd number of occurrence     
    if len(odd_l) >1:
        pass
    else:
        found = True

    return found


    # perms = set([''.join(p) for p in permutations(cstring)])
    # for p in perms:
    #     if p[::-1] == p:
    #         return True
    # return False

def run_test():
    N, Q = map(int, input().split(' '))
    fstring = input()
    found = set()
    yes = 0
    for q in range(Q):
        s, e = map(int, input().split(' '))
        cstring = fstring[s-1:e]
        if cstring in found:
            yes += 1
            continue
        if palindrome(cstring):
            yes += 1
            found.add(cstring)
    return yes


for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, run_test()))