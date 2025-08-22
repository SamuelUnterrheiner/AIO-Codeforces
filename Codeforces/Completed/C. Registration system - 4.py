a = []
name_counts = {}

for _ in range(int(input())):
    name = input()
    if name not in name_counts:
        name_counts[name] = 0
        a.append(name)
        print("OK")
    else:
        name_counts[name] += 1
        new_name = name + str(name_counts[name])
        while new_name in name_counts:
            name_counts[name] += 1
            new_name = name + str(name_counts[name])
        name_counts[new_name] = 0
        a.append(new_name)
        print(new_name)