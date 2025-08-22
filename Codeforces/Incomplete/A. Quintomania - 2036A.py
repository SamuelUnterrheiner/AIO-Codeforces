for i in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    perfect = True
    for i in range(n-1):
        if abs(A[i+1] == 5 or abs(A[i]) - A[i+1]) == 7:
            pass
        else:
            perfect = False
        
    if perfect:
        print("YES")
    else:
        print("NO")