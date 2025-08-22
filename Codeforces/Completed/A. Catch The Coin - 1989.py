num_test_cases = int(input())
for i in range(num_test_cases):
    x, y = map(int, input().split(' '))
    if y < -1:
        print("NO")
    else:
        print('YES')