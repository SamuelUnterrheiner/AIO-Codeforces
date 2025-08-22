N = int(input().strip())
word = input().strip()
 
for i in range(N):
   if word[i] == '?':
       if i < N-1:
           new_word = word[:i] + word[i+1] + word[i+1:]
       else:
           new_word = word[:i] + word[i-1]
answer = 0
for i in range(N-1):
   if new_word[i] == new_word[i+1]:
       answer += 1
print(answer)