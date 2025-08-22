for _ in range(int(input())):
    s = input().strip()
    answer = ''
    for i in range(len(s)):
        if s[i] == 'p':
            answer += 'q'
        if s[i] == 'q':
            answer += 'p'
        if s[i] == 'w':
            answer += 'w'
    answer = answer[::-1]
    print(answer)