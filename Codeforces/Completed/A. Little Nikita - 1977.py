for i in range(int(input())):
    num_split = (input()).split(" ")
    num_of_swaps = int(num_split[0])
    num_of_cubes = int(num_split[1])
    hi = num_of_swaps - num_of_cubes
    ans = 'yes'
    if num_of_cubes > num_of_swaps:
        ans = 'no'
    if not hi%2 == 0:
        ans = 'no'
    print(ans) 