for i in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))

    answer = float("inf")

    for i in range(n-1):
        answer = min(answer, max(A[i], A[i+1]))

    print(answer - 1) 