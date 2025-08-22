for _ in range(int(input())):
    n = int(input())
    a = list(input().split())
    b = list(input().split())
    b.append(0)
    answer = 0
    for i in range(n):
        if int(a[i]) > int(b[i+1]):
            answer += int(a[i]) - int(b[i+1])
    print(answer) 