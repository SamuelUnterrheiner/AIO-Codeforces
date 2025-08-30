n, l = map(int, input().split())
positions = list(map(int, input().split()))

ans = min(positions[-1], l - positions[0])
for i in range(1, n):
    left = positions[i-1]
    right = positions[i]
    t1 = 2 * left + l - right
    t2 = 2 * (l - right) + left
    if t1 < ans:
        ans = t1
    if t2 < ans:
        ans = t2
print(ans)