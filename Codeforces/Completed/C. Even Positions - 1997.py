for i in range(int(input())):
    cost = 0
    length = int(input())
    rbs = list(input())
    queue = list()
    for i in range(length):
        if i % 2 == 0:
            rbs[i] = '(' if not queue else ')'
        if rbs[i] == ')':
            cost += i - queue.pop()
        else:
            queue.append(i)
    print(cost)