for i in range(int(input())):
    n,k = map(int,input().split())
    something = max(map(int, input().split()))
    print((n - something) * 2 - (k - 1))