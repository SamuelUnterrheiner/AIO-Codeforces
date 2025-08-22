for i in range(int(input())):
    w, h, a, b = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    if x1 == x2:
        if abs(y1 - y2) % b == 0:
            print("Yes")
            continue
        else:
            print("No")
            continue

    if y1 == y2:
        if abs(x1 - x2) % a == 0:
            print("Yes")
            continue
        else:
            print("No")
            continue
    
    if (x1 - x2) % a == 0 or (y1 - y2) % b == 0:
        print("Yes")
        continue
    else:
        print("NO")