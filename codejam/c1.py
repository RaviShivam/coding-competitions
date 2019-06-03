winning_moves = {'R': 'P', 'S': 'R', 'P': 'S'}

def run_test():
    opps = int(input())
    programs = []
    for _ in range(opps):
        p = input()
        programs.append(p)
    myprogram = ''
    left_opss = programs
    for i in range(10**100):
        oppsdistinct = {}
        for j in range(len(left_opss)):
            oppmove = left_opss[j][i%len(left_opss[j])]
            if oppmove not in oppsdistinct:
                oppsdistinct[oppmove] = [j]
            else:
                oppsdistinct[oppmove] = oppsdistinct[oppmove] + [j]

        if len(oppsdistinct) == 3:
            return "IMPOSSIBLE"

        if len(oppsdistinct) == 2: 
            moves = list(oppsdistinct.keys())
            a, b  = winning_moves[moves[0]], winning_moves[moves[1]]
            countermove= a if a in moves else b
            myprogram += countermove

            remopss = [left_opss[i] for i in oppsdistinct[countermove]]
            left_opss = remopss

        if len(oppsdistinct) == 1:
            myprogram += winning_moves[list(oppsdistinct.keys())[0]]
            return myprogram

        if len(left_opss) == 0:
            return myprogram
    return 'IMPOSSIBLE'
        
        

for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, run_test()))