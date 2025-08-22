for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = int(input())
    
    ans = 'Yes'
    for i in range(n):
        if i == 0 :
            a[i] = min(a[i], b - a[i])
        else:
            if a[i-1] > min(a[i], b - a[i]):
                if a [i-1] > max(a[i], b - a [i]):
                    ans = 'No'
                    break
                else:
                    a[i] = max(a[i], b - a[i])
            else:
                a[i] = min(a[i], b - a[i])
    print(ans)