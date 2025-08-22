for i in range(int(input())):
    num_in_array = int(input())
    input_array = list(map(int, input().split()))
    answer = 0
    answer += max(input_array)
    answer += num_in_array // answer
    print(answer)