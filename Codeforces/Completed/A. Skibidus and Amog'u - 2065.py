for _ in range(int(input())):
    string_ = str(input())
    if string_[-1] == 's' and string_[-2] == 'u':
        string_ = string_[:-2] + 'i'
    print(string_) 