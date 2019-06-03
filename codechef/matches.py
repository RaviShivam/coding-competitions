play = {0: 'Ari', 1:'Rich'}

tree = {}
def construct_tree(p1, p2):
    p1, p2 = max(p1, p2), min(p1, p2)
    if p1%p2 == 0:
        return 0
    m = p1//p2

    vals = []
    print(p1, p2)
    for pm in range(m, 0, -1):
        np1, np2 = p1-pm*p2, p2
        if (np1, np2) in tree:
            vals.append((1+tree[(np1, np2)])%1)
        else:
            v = (1 + construct_tree(np1, np2))%1
            tree[(np1, np2)] = v
            vals.append(v)
    return int(any([vals]))
        

def run_test():
    p1, p2 = map(int, input().split(' '))
    v = construct_tree(p1, p2)
    return(play[v])
    
for _ in range(int(input())):
    print(run_test())
    print(tree)
    break