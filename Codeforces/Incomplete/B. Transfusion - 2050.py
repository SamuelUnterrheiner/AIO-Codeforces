for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ods = 0
    evs = 0
    for j in range(n):
        if j % 2 == 1:
            ods += a[j]
        else:
            evs += a[j]
    odc = n // 2
    evc = n // 2
    if n % 2 == 1:
        evc += 1

    if (odc == 0 or evc == 0 or
        ods % odc != 0 or
        evs % evc != 0 or
        ods // odc != evs // evc):
        print("NO")