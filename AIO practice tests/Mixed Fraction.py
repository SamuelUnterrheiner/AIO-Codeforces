a, b = map(int, input().split())
ansp1 = int(a/b).__floor__
ansp2 = ''
if a/b != ansp1:
    ansp2.__add__(str(a))
    ansp2.__add__('/')
    ansp2.__add__(str(float(a/b)-ansp1))
print(ansp1, ansp2)