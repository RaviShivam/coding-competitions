def run_case2():
    N = int(input())
    tasks_original = []
    for i in range(N):
        new_task =  tuple(map(int, input().split(' '))) + (i, )
        tasks_original.append(new_task)
    tasks = sorted(tasks_original, key=lambda x: x[0])
    C = []
    J = []
    sol = {}
    for task in tasks:
        if len(C) == 0:
            sol[task] = 'C'
            C.append(task)
            continue
        if task[0] >= C[-1][1]:
            sol[task] = 'C'
            C.append(task)
            continue
        if len(J) == 0:
            sol[task] = 'J'
            J.append(task)
            continue
        if task[0] >= J[-1][1]:
            sol[task] = 'J'
            J.append(task)
            continue
        return 'IMPOSSIBLE'
    return ''.join([sol[x] for x in tasks_original])


if __name__ == "__main__":
    for i in range(1, int(input()) + 1):
        print("Case #{0}: {1}".format(i, run_case2()))