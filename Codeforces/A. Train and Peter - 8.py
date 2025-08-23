flags = input().strip()
s1 = input().strip()
s2 = input().strip()
forwards = flags.find(s1)
if forwards != -1:
    forwards = flags.find(s2, forwards + len(s1))
else:
    forwards = -1
backwards = flags[::-1].find(s1)
if backwards != -1:
    backwards = flags[::-1].find(s2, backwards + len(s1))
else:
    backwards = -1
if forwards != -1 and backwards != -1:
    print("both")
elif forwards != -1:
    print("forward")
elif backwards != -1:
    print("backward")
else:
    print("fantasy")