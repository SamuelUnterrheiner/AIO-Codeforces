num_of_test_cases = int(input())
for i in range(num_of_test_cases):
    a, b, c, d = map(int, input().split())
    ans = "YES"
    if a > c and c > b:
        ans = "NO"
    if a > d and d > b:
        ans = "NO"
    print(ans)