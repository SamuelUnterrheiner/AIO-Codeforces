for _ in range(int(input())):
    n = int(input())
    gears = list(map(int, input().split()))
    ans = 'NO'
    for i in range(n):
        for j in range(i + 1, n):
            if gears[i] == gears[j]:
                ans = 'YES'
    print(ans)