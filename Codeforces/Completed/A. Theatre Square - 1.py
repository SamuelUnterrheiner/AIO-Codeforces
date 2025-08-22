import math
a, b, c = map(int, input().split())
tiles = math.ceil(a / c) * math.ceil(b / c)
print(tiles) 