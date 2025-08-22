input_file = open('hirein.txt', 'r')
output_file = open('hireout.txt', 'w')

x = []
s = []
m = []

n = int(input_file.readline())
for i in range(n):
    k = int(input_file.readline())
    x.append(k)

n = int(input_file.readline())
for i in range(n):
    k = int(input_file.readline())
    s.append(k)

n = int(input_file.readline())
for i in range(n):
    k = int(input_file.readline())
    m.append(k)

x = sorted(x)
s = sorted(s)
m = sorted(m)

cr = 0
xi = 0
for it in s:
    if xi >= len(x):
        break
    if x[xi] <= it:
        cr += 1
        xi += 1

mk = 0
for xi in range(xi, len(x)):
    if mk >= len(m):
        break
    if x[xi] >= m[mk]:
        cr += 1
        mk += 1

print(cr, file = output_file)

