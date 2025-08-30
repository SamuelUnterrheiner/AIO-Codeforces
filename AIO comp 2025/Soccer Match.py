a = int(input())
b = list(map(int, input().split()))
team1 = 0
team2 = 0
ans = 'NO'
for i in range(a):
    if b[i] == 1:
        team1 += 1
    else:
        team2 += 1
    if team1 > team2:
        ans = 'YES'
print(ans)