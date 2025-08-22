for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = sum(x % 2 for x in a)
    print(max(a) if c == 0 or c == n else sum(a) - c + 1)

# 