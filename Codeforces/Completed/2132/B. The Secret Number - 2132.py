for i in range(int(input())):
    b = int(input())
    a = 11
    ans = []
    while b >= a:
        if b % a == 0:
            ans.append(b // a)
        a = (a - 1) * 10 + 1
    print(len(ans))
    for i in range(len(ans) - 1, -1, -1):
        print(ans[i], end=' ')
    print()