for _ in range(int(input())):
    casinos, coins = map(int, input().split())
    max_coins = coins
    for i in range(casinos):
        min, max, profit = map(int, input().split())
        if coins >= min and coins <= max and max_coins < profit:
            max_coins = profit
    print(max_coins)