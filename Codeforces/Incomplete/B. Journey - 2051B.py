for i in range(int(input())):
    n, a, b, c = map(int, input().split())

    days = 6*(n // (a + b + c + c + b+ a))

    remaining_km = n % (a + b + c + c + b+ a)
    if remaining_km == 0:
        print(days)
    elif remaining_km <= a:
        print(days + 1)
    elif remaining_km <= a+b:
        print(days+2)
    elif remaining_km <= a+b+c:
        print(days + 3)
    elif remaining_km <= a+b+c+c:
        print(days + 4)
    elif remaining_km <= a+b+c+c+b:
        print(days + 5)
    else:
        print(days + 6)
