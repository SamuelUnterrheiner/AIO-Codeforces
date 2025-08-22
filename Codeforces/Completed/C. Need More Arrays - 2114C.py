for i in range(int(input())):
    length = int(input())
    a = list(map(int, input().split()))
    result = 0

    last = -1
    for i in a:
        if i - last > 1:
            result += 1
            last = i
    print(result)