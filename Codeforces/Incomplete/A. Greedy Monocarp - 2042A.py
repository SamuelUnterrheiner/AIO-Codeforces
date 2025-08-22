for i in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    total = 0
    i = 0
    while i < n and total + a[i] <= k:
        total += a[i]
        i += 1

    print(k - total)