for i in range(int(input())):
    n, m = map(int, input().split())
    A = []
    output_row = ''
    for i in range(n):
        row = list(map(int, input().split()))
        A.append(row)
    if n == m and m == 1:
        print('-1')
        continue
    if n > 1:
        for i in range(1, n):
            print(*A[i])
        print(*A[0])

    else:
        for i in range(n):
            print(*A[i][1:], A[i][0]) 