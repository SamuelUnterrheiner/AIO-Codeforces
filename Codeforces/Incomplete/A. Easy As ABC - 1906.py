grid = []
for _ in range(3):
    grid.append(input().strip())
lines = []
for row in grid:
    lines.append(row)
for c in range(3):
    s = ''
    for r in range(3):
        s += grid[r][c]
    lines.append(s)
s1 = ''
s2 = ''
for i in range(3):
    s1 += grid[i][i]
    s2 += grid[i][2 - i]
lines.append(s1)
lines.append(s2)
for ch in 'ABC':
    for line in lines:
        ok = True
        for letter in line:
            if letter != '.' and letter != ch:
                ok = False
        if ok:
            print(ch)
            break