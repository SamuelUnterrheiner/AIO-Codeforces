for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        if i >= 1:
            a.append(x)
            b.append(y)
    print((sum(b) + sum(a)) * 2 + (m*4)) 