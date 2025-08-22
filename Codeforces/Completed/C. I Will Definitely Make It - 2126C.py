for _ in range(int(input())):
    n, k = map(int, input().split())
    towers = list(map(int, input().split()))
    current = towers[k - 1]
    t = 0
    towers.sort()
    possible = True
    for height in towers:
        if height< current:
            continue
        t += height - current
        if t > current:
            possible = False
            break
        current = height
    print("Yes" if possible else "No")