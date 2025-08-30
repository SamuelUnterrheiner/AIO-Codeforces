first = input().split()
n = int(first[0])
d = int(first[1])
s = int(first[2])
a = list(map(int, input().split()))

hi = {}
for v in a:
    hi[v] = hi.get(v, 0) + 1

for x in a:
    while hi.get(x, 0) > 0:
        paired = False
        y = s - x
        if hi.get(y, 0) > 0:
            if y != x or hi.get(x, 0) >= 2:
                hi[x] -= 1
                hi[y] -= 1
                paired = True
                continue
        y = x + d
        if hi.get(y, 0) > 0:
            if y != x or hi.get(x, 0) >= 2:
                hi[x] -= 1
                hi[y] -= 1
                paired = True
                continue
        y = x - d
        if hi.get(y, 0) > 0:
            if y != x or hi.get(x, 0) >= 2:
                hi[x] -= 1
                hi[y] -= 1
                paired = True
                continue

        if not paired:
            print("NO")
            exit()

print("YES")
