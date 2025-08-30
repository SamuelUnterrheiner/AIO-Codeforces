n = int(input())
d = sorted(map(int, input().split()))
lo = max(d)
hi = lo + n
while lo < hi:
    mid = ((lo + hi) // 2)
    i = n - 1
    if d[i] > mid:
        lo = mid + 1
        continue
    i -= 1
    k = mid - 1
    ok = True
    while k > 0 and i >= 0:
        for _ in (0, 1):
            if i < 0: break
            if d[i] <= k:
                i -= 1
            else:
                ok = False
                break
        if not ok: break
        k -= 1
    if i >= 0: ok = False
    if ok:
        hi = mid
    else:
        lo = mid + 1
print(lo)