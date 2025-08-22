a = int(input())
c = 0
for i in range (a):
    b = input()
    b = b.split(" ")
    if b[0] < b[1] and b[1] < b[2]:
        print("STAIR")
    elif b[0] < b[1] and b[1] > b[2]:
        print("PEAK")
    else:
        print("NONE") 