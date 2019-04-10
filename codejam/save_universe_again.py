def damage(program):
    # beam power and total damage
    p, d = 1, 0
    for action in program:
        p = p*2 if action is 'C' else p # shoot
        d = d+p if action is 'S' else d # charge
    return d

def run_test():
    D, program = input().split()
    D = int(D)
    rprogram = program[::-1]
    lrprogram = list(reversed(program))

    if damage(program) <= D:
        return 0
    switches = 0

    while True:
        i = rprogram.find('SC')
        if i == -1 or damage(rprogram[::-1]) <= D:
            break
        lrprogram[i:i+2] = 'CS'
        switches += 1
        rprogram = ''.join(lrprogram)

    return switches if damage(rprogram[::-1]) <= D else 'IMPOSSIBLE'

for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, run_test()))