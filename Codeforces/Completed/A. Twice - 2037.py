for i in range(int(input())):
    n = int(input())
    a = input().split() 

    counter = {}
    for number in a:
        counter[number] = counter.get(number, 0) + 1

    answer = 0
    for number, count in counter.items():
        answer += count // 2
    print(answer)