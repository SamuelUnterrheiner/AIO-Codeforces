input_file = open('snakein.txt', 'r')
output_file = open('snakeout.txt', 'w')

DNA_num = int(input_file.readline())
DNA_string = input_file.readline().split()

sequence = "SNAKE"
max_dna = 0
cur_letter = 0
sequence_index = 0

for i in range(DNA_num):
    cur_id = DNA_string[cur_letter]
    if sequence_index == (cur_id.find(DNA_string)) - 1:
        sequence_index += 1
    if sequence_index == len(sequence):
        max_dna += 1

print(max_dna, file = output_file)
