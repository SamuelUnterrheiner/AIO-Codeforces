for _ in range(int(input())):
    input_ = int(input())
    answer = 1
    while(input_ > 3):
        input_ = input_ // 4
        answer *= 2
    print(answer) 