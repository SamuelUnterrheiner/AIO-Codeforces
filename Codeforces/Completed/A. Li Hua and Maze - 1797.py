for i in range(int(input())):
    n, m, = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    if (x1 == 1 or x1 == n) and (y1 == 1 or y1 == m):
        surround1 = 2
    elif x1 == 1 or x1 == n or y1 == 1 or y1 == m:
        surround1 = 3
    else:
        surround1 = 4
    
    if (x2 == 1 or x2 == n) and (y2 == 1 or y2 == m):
        surround2 = 2
    elif x2 == 1 or x2 == n or y2 == 1 or y2 == m:
        surround2 = 3
    else:
        surround2 = 4

    print(min(surround1, surround2))
     