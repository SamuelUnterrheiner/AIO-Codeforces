rook = list(input())
knight = list(input())
rx, ry = rook[0], rook[1]
kx, ky = knight[0], knight[1]

alphabet = 'a b c d e f g h'.split()
rx = alphabet.index(rx)
kx = alphabet.index(kx)
ry, ky = int(ry) - 1, int(ky) - 1

attacked = set()

for i in range(8):
    attacked.add((rx, i))
    attacked.add((i, ry))

knight_moves = [[kx-1, ky-2], [kx-2, ky-1], [kx+1, ky-2], [kx+2, ky-1], [kx-1, ky+2], [kx-2, ky+1], [kx+1, ky+2], [kx+2, ky+1]]
for pos in knight_moves:
    if 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
        attacked.add((pos[0], pos[1]))

rook_knight_moves = [[rx-1, ry-2], [rx-2, ry-1], [rx+1, ry-2], [rx+2, ry-1], [rx-1, ry+2], [rx-2, ry+1], [rx+1, ry+2], [rx+2, ry+1]]
for pos in rook_knight_moves:
    if 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
        attacked.add((pos[0], pos[1]))

attacked.add((rx, ry))
attacked.add((kx, ky))

ans = 64 - len(attacked)
print(ans)