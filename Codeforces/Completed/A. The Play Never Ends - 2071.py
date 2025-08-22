for i in range(int(input())):
    match_number = int(input())
    answer = 'no'
    if match_number % 3 == 1:
        answer = 'yes'
    print(answer) 