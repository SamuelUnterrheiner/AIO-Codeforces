t = int(input())
for i in range(t):
    n = int(input())
    coins = input()

    if coins.count("U") % 2 == 1:
        print("Yes")
    else:
        print("NO")