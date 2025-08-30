a = []
b = []

n, l = map(int, input().strip().split())
for i in range(n):
    input_vars = list(map(int, input().strip().split()))
    a.append(input_vars[0])
    b.append(input_vars[1])
ans = min(b) - max(a) + 1
if ans < 0:
    ans = 0
print(ans)