input_file = open('sitin.txt', 'r')
output_file = open('sitout.txt', 'w')

a, b, = map(int, input_file.readline().split())
c = int(input_file.readline())

d = a*b

e = c-d
if d > c:
    f = e
else:
    f = d
print(f, e, file= output_file)