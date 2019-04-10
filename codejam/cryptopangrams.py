import itertools

def is_Prime(n):
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            return False
    return True

def find_first_primes(val):
    for v in range(2, val):
        if val%v==0 and is_Prime(v):
            return [v, int(val/v)]

def construct_chain(crypt, start):
    chain = []
    chain.append(start[0])
    chain.append(start[1])
    for case in crypt[1:]:
        a = case/chain[-1]
        if a%1 != 0:
            return False
        chain.append(int(a))
    return chain
    
def run_test():
    N, L = map(int, input().split(' '))
    crypt = list(map(int, input().split(' ')))
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    startchain= find_first_primes(crypt[0])
    chain = construct_chain(crypt, startchain)
    chain = chain if chain else construct_chain(crypt, startchain[::-1])

    # Construct message
    message = ''
    messagemap = dict(zip(sorted(set(chain)), alphabet))
    for m in chain:
        # if m in messagemap:
        message += messagemap[m]
    return message

        
for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, run_test()))
