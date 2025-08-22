input_file = open('addin.txt', 'r')
output_file = open('addout.txt', 'w')

a, b = map(int, input_file.readline().split())

print(a+b, file = output_file)