for _ in range(int(input())):
    s = [int(x) for x in input()]
    sm = sum(s)
    twos = s.count(2)
    threes = s.count(3)
    found = False
    for i in range(min(10, twos + 1)):
        for j in range(min(10, threes + 1)):
            if (sm + i * 2 + j * 6) % 9 == 0:
                print('YES')
                found = True
                break
        if found:
            break
    else:
        print('NO')
