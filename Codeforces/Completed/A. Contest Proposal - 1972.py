t = int(input())

for i in range(t):

    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    added = 0

    i = 0
    j = 0
    while j < n:
        if A[i] <= B[j]:
            i += 1
            j += 1
        else:
            added += 1
            j += 1
        
    print(added)