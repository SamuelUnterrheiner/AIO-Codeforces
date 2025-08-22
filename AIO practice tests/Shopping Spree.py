N, K = map(int, input().strip().split())
costs = list(map(int, input().strip().split()))
 
answer = 0
for i in range(K):
   answer += costs[i]
 
for i in range(K+1, N-K, 2):
   answer += costs[i]

print(answer)