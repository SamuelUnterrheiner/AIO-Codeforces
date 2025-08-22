for i in range(int(input())):
    n, k = map(int, input().split())

    if k == 1:
        print(n)
        continue

    number = []
    while n > 0:
        number.append(n%k)
        n //= k
    number.reverse()
    print(sum(number)) 