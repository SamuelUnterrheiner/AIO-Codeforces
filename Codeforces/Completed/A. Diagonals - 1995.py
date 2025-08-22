for i in range(int(input())):
    n, k = map(int, input().split())
    a = n
    b = n-1
    answer = 0
    while k > 0:
        k -= a
        answer += 1
        a, b = b, (b if a != b else b - 1)
    print(answer) 