n = int(input())
d = list(map(int, input().split()))
maxD = max(d)
freq = [0]*(maxD+1)
for problem in d:
    freq[problem] += 1
ans = 0
Ni = 0
for i in range(maxD, 0, -1):
    Ni += freq[i]
    candidate = (Ni // 2) +1
    if candidate > ans:
        ans = candidate
print(ans)