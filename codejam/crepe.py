import operator
dirc = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
def run_test():
    def fill_locs(lx, ux, ly, uy):
        for x in range(lx, ux+1):
            for y in range(ly, uy+1):
                possible_crepes[(x, y)] = 1 if (x, y) not in possible_crepes else possible_crepes[(x,y)] + 1

    P, Q = map(int, input().split(' '))
    possible_crepes = {}
    for p in range(P):
        x, y, d = input().split(' ')
        x, y = int(x), int(y)
        move = dirc[d]
        nx, ny = x+move[0], y+move[1]
        if d=='N':
            fill_locs(0, Q, ny, Q)
        if d=='S':
            fill_locs(0, Q, 0, ny)
        if d=='E':
            fill_locs(nx, Q, 0, Q)
        if d=='W':
            fill_locs(0, nx, 0, Q)
    mx, my = -1, -1
    mc = -1
    for (fx, fy), v in possible_crepes.items():
        if (v > mc) or (fx < mx and mc >= v and fy <= my) or (fy < my and fx<=mx and mc >= v):
            mc = v
            mx, my = fx, fy
    return mx, my

for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, run_test()))
    # break
