for _ in range(int(input())):
    a, b = map(int, input().split())
    c = []
    for i in range(a):
        c.append(list(map(int, input().split())))
    d1 = {}
    d2 = {}
    for i in range(a):
        for j in range(b):
            d1[i - j] = d1.get(i - j, 0) + c[i][j]
            d2[i + j] = d2.get(i + j, 0) + c[i][j]
    ans = 0
    for i in range(a):
        for j in range(b):
            ans = max(ans, d1[i - j] + d2[i + j] - c[i][j])
    print(ans)
