for i in range(int(input())):
    size, num_rooks = map(int, input().split())
    for i in range(num_rooks):
        sizea, num_rooksa = map(int, input().split())
    if (num_rooks + 1) <= size:
        print('YES')
    else:
        print('NO') 