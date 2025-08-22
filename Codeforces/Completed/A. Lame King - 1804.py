for i in range(int(input())):
    x, y = map(abs, map(int, input().split(' ')))
    answer = max(x, y)*2
    if x != y:
        answer -= 1
    print(answer) 