for i in range(int(input())):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(abs(a - c), abs(a - d), abs(b-c), abs(b-d)))