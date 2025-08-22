for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    count_odd = 0
    for i in nums:
        if i % 2 == 1:
            count_odd += 1
    if count_odd == n:
        print(count_odd - 1)
    else:
        print(count_odd + 1)
         