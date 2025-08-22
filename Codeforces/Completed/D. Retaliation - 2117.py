for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    diff = a[1] - a[0]
    hi = False
    for i in range(2, n):
        if diff!=a[i]-a[i-1]:
            hi = True

    if hi == True:
        print("NO")
    else:
        for i in range(n):
            a[i] = a[i]+(diff*(n-i) if diff<0 else -diff*(i+1))

        print("YES"if a[0]>=0 and a[0]%(n+1)==0 else"NO")