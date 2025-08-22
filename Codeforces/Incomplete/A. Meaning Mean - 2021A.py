for i in range(int(input)):
    n = int(input())
    A = list(map(int, input().split()))
    
    A.sort()
    
    answer = (A[0] + A[1]) // 2
    for i in range(2, n):
        answer = (answer + A[i]) // 2
    
    print(answer)