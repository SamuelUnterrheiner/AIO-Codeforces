for i in range(int(input())):
    n, s, m = map(int, input().split())

    L = []
    R = []

    for i in range(n):
        li, ri = map(int, input().split())
        L.append(li)
        R.append(ri)

    answer = "NO"
    if L[0] >= s:
        answer = "Yes"
    elif  m - R[-1] >= s:
        answer = "Yes"
    for i in range(n-1):
        if L[i+1] - R[i] >= s:
            answer = "YES"
    
    print(answer)