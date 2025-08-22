for _ in range(int(input())):
    n = int(input())
    nums = map(int, input().split())
    sort_nums = sorted(nums)
    ans = []

    found_leg = False
    for i in range(1, len(sort_nums)):
        if sort_nums[i - 1] == sort_nums[i]:
            a = sort_nums.pop(i - 1)
            b = sort_nums.pop(i - 1)
            ans = [a, b]
            found_leg = True
            break
    if not found_leg:
        print(-1)
        continue

    found_base = False
    for j in range(1, len(sort_nums)):
        if sort_nums[j] - sort_nums[j-1] < 2 * a:
            ans.append(sort_nums[j-1])
            ans.append(sort_nums[j])
            found_base = True
            break

    if not found_base or len(ans) < 4:
        print(-1)
    else:
        print(*ans)