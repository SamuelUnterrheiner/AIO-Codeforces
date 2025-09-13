for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print((n-1) * (max(a) - min(a)))