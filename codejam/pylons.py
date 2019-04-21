from random import shuffle
def valid_move(past, curr):
    a = (past[0]==curr[0]) or (past[1]==curr[1]) or (past[0] - past[1] == curr[0] - curr[1]) or (past[0] + past[1] == curr[0] + curr[1])
    return not a

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

all_perm_moves = all_perms([(-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2),(1, -2)])

def run_test():
    r, c = map(int, input().split(' '))
    for moves in all_perm_moves:
        lst, tour, visited = (1, 1), [(1,1)], set([(1,1)])
        current = None
        while True:
            fnd = None
            for m in moves:
                current = (1+(lst[0]+m[0]-1)%r, 1+(lst[1]+m[1]-1)%c)
                if current not in visited and valid_move(lst, current):
                    visited.add(current)
                    fnd = True
                    break
            if fnd is None: break
            tour.append(current)
            lst = current
        
        if len(visited) == r*c:
            return 'POSSIBLE', tour

    return 'IMPOSSIBLE', list()

def randomtest():
    r, c = map(int, input().split(' '))
    mat = []
    for x in range(1, r+1):
        for y in range(1, c+1):
            mat.append((x, y))
    for _ in range(1000):
        shuffle(mat)
        unvisited = set(range(1, len(mat)))
        seq = [mat[0]]
        while True:
            fnd = False
            for x in unvisited:
                if valid_move(seq[-1], mat[x]):
                    seq.append(mat[x])
                    unvisited.remove(x)
                    fnd = True
                    break
            if not fnd or len(unvisited) == 0:
                break
            
        if len(seq) == len(mat):
            return "POSSIBLE", seq
    
    return 'IMPOSSIBLE', list()

for i in range(1, int(input()) + 1):
    a, l = randomtest()
    # a, l = run_test()
    print("Case #{}: {}".format(i, (a)))
    for e in l:
        print(*e)