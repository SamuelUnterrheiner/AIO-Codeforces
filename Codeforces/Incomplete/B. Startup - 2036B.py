for i in range(int(input())):
    shelves, bottles = map(int, input().split())
    brand = []
    cost = []
    for i in range(bottles):
        x, y = map(int, input().split())
        brand.append(x)
        cost.append(y)
    