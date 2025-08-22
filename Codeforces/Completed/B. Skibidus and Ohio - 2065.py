for _ in range(int(input())):
    s = input().strip()
    check = False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            check = True
            break
    if check:
        print(1)
    else:
        print(len(s))