for i in range(int(input())):
    n, a, b = map(int, input().split())
    answer = 'NO'
    x = abs(a-b)
    if x % 2 == 0:
        answer = 'YES'
    print(answer)