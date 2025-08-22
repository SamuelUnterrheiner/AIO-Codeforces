for i in range(int(input())):
    x, m = map(int, input().split())
    ans = 0
    for y in range(1, min(2 * x, m) + 1):
        if x != y and (x % (x ^ y) == 0 or y % (x ^ y) == 0):
            ans = 1
    print(ans)