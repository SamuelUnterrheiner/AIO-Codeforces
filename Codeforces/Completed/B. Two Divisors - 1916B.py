import math
for i in range(int(input())):
    a, b = map(int, input().split())
    if b % a == 0:
        print(int(b*b / a))
    else:
        print(int((a*b) / math.gcd(a, b)))