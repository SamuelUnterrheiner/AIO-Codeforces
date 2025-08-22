for _ in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))
    hi = b[0]
    yn = 1
    for bob in b:
        if bob>=2*hi:
            yn=2
            break
        hi = min(hi, bob)
    if yn == 1:
        print("YES")
    else:
        print("NO")