for i in range(int(input())):
    s = str(input())
    if s[1] == '<':
        if s[0] < s[2]:
            print(s)
        elif s[0] == s[2]:
            print(s[0] + '=' + s[2])
        else:
            print(s[0] + '>' + s[2])
    if s[1] == '=':
        if s[0] == s[2]:
            print(s)
        else:
            print(s[2] + '=' +  s[2])
    if s[1] == '>':
        if s[0] > s[2]:
            print(s)
        elif s[0] == s[2]:
            print(s[0] + '=' + s[2])
        else:
            print(s[0] + '<' + s[2]) 
