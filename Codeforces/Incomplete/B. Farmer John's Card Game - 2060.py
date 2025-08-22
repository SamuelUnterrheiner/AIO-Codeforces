for _ in range(int(input)):
    n, m = map(int, input().split())

    cows = []
    for i in range(n):
        cards = list(map(int, input().split()))
        cows.append(cards)

    violation = False
    for i in range(n):
        cows[i].sort()
        for j in range(m-1):
            if cows[i][j+1] - cows[i][j] != n:
                violation = True
    
    if violation:
        print(-1)
        continue
    turn_order = [None] * n
    for i in range(n):
        turn_order[min(cows[i])] = i +1
    
    print(*turn_order)