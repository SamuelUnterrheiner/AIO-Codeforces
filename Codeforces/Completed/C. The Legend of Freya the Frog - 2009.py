import math
for i in range(int(input())):
    x, y, k = map(int, input().split())
    answer = 0
    a = math.ceil(x/k)
    b = math.ceil(y/k)
    answer = max(a, b)
    answer *= 2
    if b < a:
        answer -= 1
    print(answer)