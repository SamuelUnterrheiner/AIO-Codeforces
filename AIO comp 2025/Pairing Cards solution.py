from collections import Counter
def possible(D, S, A):
    freq = Counter(A)
    print(freq)
    values = sorted(freq.keys)
    for x in values:
        while freq[x]>0:
            paired = False
            if D>0 and freq[x+D]>0:
                freq[x]-=1
                freq[x+D]-=1
                paired = True
            elif S-x in freq and freq[S-x] > 0:
                freq[x] -= 1
                freq[S+D] -= 1
                paired = True
            else:
                return False
    return paired 
N, D, S = tuple(map(int, input().split()))
A = list(map(int, input().split()))
if possible(D, S, A):
    print("YES")
else:
    print("NO")