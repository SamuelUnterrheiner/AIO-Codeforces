import math
for i in range(int(input())):
    x = int(input())
    y, z = map(int, input().split())
    a = min(y, z)
    a = x/a
    a = math.ceil(a)
    print(a)