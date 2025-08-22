for i in range(int(input())):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    total = sum(c)
    c.sort()
    c[-1] -= 1
    c.sort()
    if c[-1] - c[0] > b or total % 2 == 0:
        print("Jerry")
    else:
        print("Tom")
        