days, sum_time = map(int, input().split())
min_study = []
max_study = []
for i in range(days):
    a, z = map(int, input().split())
    min_study.append(a)
    max_study.append(z)

min_total = sum(min_study)
max_total = sum(max_study)

if not (min_total <= sum_time <= max_total):
    print('NO')
else:
    print('YES')
    res = min_study[:]
    left = sum_time - min_total
    for i in range(days):
        add = min(max_study[i] - min_study[i], left)
        res[i] += add
        left -= add
    print(' '.join(map(str, res)))
##### Accepted #####