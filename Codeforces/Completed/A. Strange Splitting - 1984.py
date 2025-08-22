for i in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    if A[0] == A[-1]:
        print("NO")
    else:
        print("YES")
        print("B" + "R" + "B" * (n - 2)) 