for i in range(int(input())):
    a = int(input())
    b = 0
    for i in range(3):
        if a >= i:
            b += (a - i) // 15 + 1
    print(b) 