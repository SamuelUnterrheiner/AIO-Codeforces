for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = [a[i] - b[i] for i in range(n)]
    d.sort()
    ans = 0
    l, r = 0, n - 1
    while l < r:
        if d[l] + d[r] >= 0:
            ans += 1
            l += 1
            r -= 1
        else:
            l += 1
    print(ans)
# haydon - 50%
# me - 95%
# william - 50%