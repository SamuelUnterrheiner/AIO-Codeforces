n = int(input())
groups = list(map(int, input().split()))
count4 = groups.count(4)
count3 = groups.count(3)
count2 = groups.count(2)
count1 = groups.count(1)
jeffs = count4
bobs = min(count3, count1)
jeffs += bobs
count3 -= bobs
count1 -= bobs
jeffs += count3
jeffs += count2 // 2
count2 %= 2
if count2:
    jeffs += 1
    count1 -= min(2, count1)
if count1 > 0:
    jeffs += (count1 + 3) // 4
print(jeffs)