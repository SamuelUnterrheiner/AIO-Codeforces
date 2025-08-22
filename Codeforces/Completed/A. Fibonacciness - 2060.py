for i in range(int(input())):
    row = list(map(int, input().split()))
    missing_item = row[3] - row[2]

    answer1 = 0
    answer2 = 0
    answer3 = 0
    row.insert(2, missing_item)
    if row[2] == (row[0] + row[1]):
        answer1 += 1
    if row[3] == (row[1] + row[2]):
        answer1 += 1
    if row[4] == (row[2] + row[3]):
        answer1 += 1

    missing_item = row[3] - row[1]
    row[2] = missing_item
    if row[2] == (row[0] + row[1]):
        answer2 += 1
    if row[3] == (row[1] + row[2]):
        answer2 += 1
    if row[4] == (row[2] + row[3]):
        answer2 += 1

    missing_item = row[4] - row[3]
    row[2] = missing_item
    if row[2] == (row[0] + row[1]):
        answer3 += 1
    if row[3] == (row[1] + row[2]):
        answer3 += 1
    if row[4] == (row[2] + row[3]):
        answer3 += 1
    print(max(answer2, answer1, answer3)) 