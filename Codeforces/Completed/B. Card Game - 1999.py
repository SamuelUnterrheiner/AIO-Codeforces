def f(a, b):
    if (a > b): return 1
    if (a == b): return 0
    if (a < b): return -1
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    ans = 0
    if f(a, c) + f(b, d) > 0:
        ans += 1
    if f(a, d) + f(b, c) > 0:
        ans += 1
    if f(b, c) + f(a, d) > 0:
        ans += 1
    if f(b, d) + f(a, c) > 0:
        ans += 1
    print(ans)
for i in range(int(input())):
    a, b, c, d = map(int, input().split)
    answer = 0
    