for i in range(int(input())):
    n, c, d = map(int, input().split())
    b = list(map(int(input().split())))

    progressive_square = [int (b)]
    for i in range(n-1):
        progressive_square.append(progressive_square[-1] + d)
    for i in range(n-1):
        progressive_square.append(progressive_square[-n] + c)
    
    progressive_square.sort()
    b.sort()
    if progressive_square == b:
        print("YES")
    else:
        print("NO")