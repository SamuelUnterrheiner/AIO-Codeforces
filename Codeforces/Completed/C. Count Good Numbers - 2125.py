for i in range(int(input())):
    min, max = map(int, input().split())
    total = max - min + 1
    ans = total
    primes = [2, 3, 5, 7]
    for a in range(4):
        mul = primes[a]
        count = max // mul - (min - 1) // mul
        ans -= count
    for a in range(4):
        for b in range(a + 1, 4):
            mul = primes[a] * primes[b]
            count = max // mul - (min - 1) // mul
            ans += count
    for a in range(4):
        for b in range(a + 1, 4):
            for c in range(b + 1, 4):
                mul = primes[a] * primes[b] * primes[c]
                count = max // mul - (min - 1) // mul
                ans -= count
    mul = primes[0] * primes[1] * primes[2] * primes[3]
    count = max // mul - (min - 1) // mul
    ans += count
    print(ans)