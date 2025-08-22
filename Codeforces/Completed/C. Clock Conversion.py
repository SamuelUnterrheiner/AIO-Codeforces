num = int(input())
for i in range (num):
    a = input()
    a = list(map(int, a.split(":")))
    if a[0] > 12:
        type1 = str(" PM")
        a[0] -= 12
    elif a[0] < 12:
        type1 = str(" AM")
    elif a[0] == 12:
        type1 = str(" PM")
    if a[0] == 0:
        a[0] = 12
    print(f"{a[0]:02}:{a[1]:02}{type1}")
