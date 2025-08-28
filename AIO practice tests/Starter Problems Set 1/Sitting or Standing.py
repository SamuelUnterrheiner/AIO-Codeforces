a, b = map(int, input().split())
c = int(input())
seats = a * b
sitting = min(c, seats)
standing = max(0, c - seats)
print(sitting, standing)