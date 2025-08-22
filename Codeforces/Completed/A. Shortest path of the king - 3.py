start, end = input(), input()
x1, y1 = ord(start[0]) - ord('a'), int(start[1]) - 1
x2, y2 = ord(end[0]) - ord('a'), int(end[1]) - 1

dx = x2 - x1
dy = y2 - y1

steps = max(abs(dx), abs(dy))
print(steps)

moves = []
for _ in range(steps):
    move = ''
    if dx > 0:
        move += 'R'
        dx -= 1
    elif dx < 0:
        move += 'L'
        dx += 1
    if dy > 0:
        move += 'U'
        dy -= 1
    elif dy < 0:
        move += 'D'
        dy += 1
    moves.append(move)

for move in moves:
    print(move) 