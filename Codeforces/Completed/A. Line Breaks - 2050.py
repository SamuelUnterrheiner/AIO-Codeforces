for _ in range(int(input())):
    n, m = map(int, input().split())
    words = [input().strip() for _ in range(n)]
    total = 0
    x = 0
    for word in words:
        if total + len(word) <=m:
            total += len(word)
            x += 1
        else:
            break
    print(x) 