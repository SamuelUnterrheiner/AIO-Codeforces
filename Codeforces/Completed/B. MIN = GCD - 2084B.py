import math
for _ in range(int(input())):
    a = int(input())
    input_list = list(map(int, input().split()))
    b = input_list.index(min(input_list))
    c = 0
    for i in range(a):
        if i != b and input_list[i] % input_list[b] == 0:
            c = math.gcd(c, input_list[i])
    if c == input_list[b]:
        print("Yes")
    else:
        print("No")
