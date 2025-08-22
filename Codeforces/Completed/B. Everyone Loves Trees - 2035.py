for i in range(int(input())):
    n = int(input())
    if n == 1 or n == 3:
        print("-1")
    elif n % 2 == 0:
        print("3" * (n - 2) + "66")
    else:
        print("3" * (n - 5) + "36366")

