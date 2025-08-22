for i in range(int(input())):
    n = int(input())
    matrix = []
    answer = []
    for i in range(n):
        matrix.append(input())
    matrix.reverse()
    for i in range(n):
        for x in range(4):
            if matrix[i][x] == '#':
                answer.append(x + 1)
    print(*answer)