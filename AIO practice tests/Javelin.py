N = int(input().strip())
D = list(map(int, input().strip().split()))
answer = 0
cur_highest = 0
for i in range(N):
    if D[i] > cur_highest:
        answer += 1
        cur_highest = D[i]
print(answer)