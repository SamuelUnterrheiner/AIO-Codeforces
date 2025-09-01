n, m = map(int, input().split())
markers = []
for _ in range(n):
    x, y = map(int, input().split())
    markers.append((x, y))

caps_diam = {}
caps_colordiam = {}

for _ in range(m):
    a, b = map(int, input().split())
    caps_diam[b] = caps_diam.get(b, 0) + 1
    key = (a, b)
    caps_colordiam[key] = caps_colordiam.get(key, 0) + 1

marker_count = {}
for x, y in markers:
    key = (x, y)
    marker_count[key] = marker_count.get(key, 0) + 1

jeffs = 0
bobs = 0

for key in marker_count:
    match = min(marker_count[key], caps_colordiam.get(key, 0))
    if match > 0:
        bobs += match
        jeffs += match
        caps_diam[key[1]] -= match

for x, y in markers:
    key = (x, y)
    if caps_colordiam.get(key, 0) > 0:
        caps_colordiam[key] -= 1
        continue
    if caps_diam.get(y, 0) and caps_diam[y] > 0:
        jeffs += 1
        caps_diam[y] -= 1

print(jeffs, bobs)