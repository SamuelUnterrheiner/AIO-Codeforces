for _ in range(int(input())):
    a, b = map(int, input().split())
    grid = []
    for _ in range(a):
        row = list(map(int, input().split()))
        grid.append(row)

    diag1 = {}
    diag2 = {}
    for i in range(a):
        for j in range(b):
            diag1[i-j] = diag1.get(i-j, 0) + grid[i][j]
            diag2[i+j] = diag2.get(i+j, 0) + grid[i][j]

    max_sum = 0
    for i in range(a):
        for j in range(b):
            s = diag1[i-j] + diag2[i+j] - grid[i][j]
            max_sum = max(max_sum, s)
    print(max_sum)