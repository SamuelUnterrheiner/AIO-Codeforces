for _ in range(int(input())):
    n = int(input())
    chicken = list(map(int, input().split()))
    chicken.sort()
    ans = 0
    for i in range(n - 1, -1, -2):
        ans += chicken[i]
    print(ans)