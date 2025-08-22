for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    left = 0
    check = True
    while left < n-1:
        if nums[left] > nums[left=1]:
            chek = False
            break
        else:
            nums[left+1] -= nums[left]
            nums[left] = 0
            left += 1
    if check:
        print('Yes')
    else:
        print('No')