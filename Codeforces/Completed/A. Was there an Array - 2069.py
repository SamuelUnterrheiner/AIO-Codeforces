for i in range(int(input())):
    a = int(input())
    b = list(input().split())
    ans = 'yes'
    for i in range(len(b) - 2):
        if b[i] == '1' and b[i+1] == '0' and b[i+2] == '1':
            ans = 'no'

    print(ans)