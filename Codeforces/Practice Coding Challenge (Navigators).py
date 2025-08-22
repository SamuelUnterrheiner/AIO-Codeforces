# ###################      My solutions     ####################

# ######### Full Name ##########
# fname = input()
# lname = input()
# print(fname, lname)

# ######### Same Close Different ##########
# num1 = int(input())
# num2 = int(input())
# if num1 == num2:
#     print('same')
# elif abs(num1 - num2) == 1:
#     print('close')
# else:
#     print('different')

# ######### Square List ##########
# num = int(input())
# answer = ''
# for i in range(2, num + 1):
#     answer += str(i * i) + ' '
# answer = answer[:-1]
# print(answer)

# ######### Too Short ##########
# answer = 0
# length = int(input())
# for i in range(length):
#     x = float(input())
#     if x >= 1.2:
#         answer += 1
# print(answer)

# ######### How Many Inputs? ##########
# x = 0
# ans1 = 0
# ans2 = 0
# while(x != -1):
#     x = int(input())
#     ans1 += 1
#     ans2 += x
# print(ans1 - 1)
# print(ans2 + 1)

# ######### Only Integers ##########
# num = input()
# if num.isdigit():
#     print('integer')
# else:
#     print('not an integer')

# ######### Countdown ##########
# num = int(input())
# for i in range(num, 0, -1):
#     print(i)
# print('lift off')

# ######### Solar Panels ##########
# width = float(input())
# height = float(input())
# print((int(height/1.5)) * (int(width/0.95)))

# ######### Counting Letters ##########
# s = input()
# ans1 = 0
# ans2 = 0
# for ch in s:
#     if ch.lower() in 'aeiou':
#         ans1 += 1
#     elif ch.lower() in 'bcdfghjklmnpqrstvwxyz':
#         ans2 += 1
# print(ans1, ans2)

# ######### Pig Lattin ##########
# text = str(input())
# x = ''
# ans = text
# if text.lower().startswith('a') or text.lower().startswith('e') or text.lower().startswith('i') or text.lower().startswith('o') or text.lower().startswith('u'):
#     text = text + '-yay'
# else:
#     x = text[0]
#     text = text[1:]
#     text = text + '-'
#     text += x
#     text += 'ay'
# print(text)


####################     Questions and proposed answers     ####################
'''
Full Name

Task
Write a program that takes as input a person's first name and their last name. Your program should then output their full name by combining the two inputs separated by a space. 

Input format
Two lines; the first line will contain a first name and the scond line will contain a last name. 

Output format
A single line containing the two names separated by a space. 

Example
Input:
Mo
Ali
Output:
Mo Ali


# get input
fname = input()
lname = input()

# output
print(fname, lname)



Same Close Different

Task
Write a program that compares two numbers and outputs whether they are the "same", "close" or "different". 

The two numbers are the "same" if they equal to each other.
The two numbers are "close" if they are within 1 of each other. (e.g. 3 and 4, or 4 and 3)
The two numbers are "different" if the difference between them is greater than 1.
Input format
Two numbers on separate lines. 

The numbers will always be valid integers in the range 0 to 1000.
Output format
One of three strings:

"same"
"close"
"different"
Example
Input:
3
3
Output:
same


# get input:
a = int(input())
b = int(input())

if a == b:
    print("same")
elif a-b == 1 or b-a == 1:
    print("close")
else:
    print("different")




Square List

Introduction:
A "square number" is a number which is the square of an integer value. For example, the number 16 is a square number because it is 42.

Task:
Write a program that outputs a list of all the square numbers between 22 and n2 (inclusive). The value for n will be a positive integer in the range 3 to 1000. 

Input format:
A single number (positive integer) in the range 3 to 1000. 

Output format: 

A list of numbers. Each number will be a "square number". 

Example
Input:
10
Output:
4 9 16 25 36 49 64 81 100


# Get input.
n = int(input())

my_string = ""

for i in range(2, n+1, 1):
    my_string = my_string + str(i**2) + " "

# Output the list after first removing the trailing space.
print(my_string[:-1])



Too Short

Introduction
Children are only allowed on a fairground ride if they are at least 1.2m tall. There is a line of children waiting to have a ride. 

Task
Write a program that counts how many children in the queue will be allowed on the ride.

Input format
The first line of input is a number (positive integer) that indicates how many children (n) are in the queue.
The next n rows each contain a decimal number (float) which represents the height of each child in the queue.
Output format
An integer indicating the number of children who are tall enough for the ride. 
Example
Input
4
1.41
1.20
1.19
1.21
Output
3


n = int(input())
counter = 0

for i in range(n):
    if float(input()) >= 1.2:
        counter += 1

print(counter)




How Many Inputs?

Introduction
When a series of data values are being collected, it is common to ask the user to enter a rogue value to indicate the end of the data input.

For example the user might be asked to enter a series of positive integers and indicate when the data has all been entered by entering -1.

Task
Write a program that takes an series of data values (positive integers) terminating in -1. The program should then output:

a count of the data values entered (excluding the rogue value -1)
the sum of the data values enetered  (excluding the rogue value -1)
Input format
Several lines of input. Each line will contain a single positive unsigned integer, until the last line which will contain -1. 

Output format: 

Two lines: 

the first line will display the count of data values entered (as a positive unsigned integer)
the second line will display the sum of data values entered (as a positive unsigned integer)
Example
Input
5
7
4
-1
Output
3
16


counter = 0
total = 0

while True:
    n = int(input())
    if n >= 0:
        counter += 1
        total = total + n
    else:
        break

print(counter)
print(total)



Only Intigers

Introduction
An integer is a whole number. For example 3, 15 and 22 are integers.

The value 7.3 is not an integer, it is a real number (sometimes called a decimal or float). 

Task
Write a program that takes a numeric value as input and outputs whether or not the value entered is a whole number.

Input format
A single number in the range 0 to 100. The number can be an integer or a real number. 
Output format:
The message "integer" if the input value was an integer or "not an integer" if the value entered was not an integer. 
Example 1
Input
1
Output
integer
Example 2
Input
5.1
Output
not an integer
Example 3
Input
5.0
Output
not an integer


num = input()
digits = "1234567890"
msg = "integer"

for char in num:
    if char not in digits:
        msg = "not an integer"

print(msg)



Countdown

Task:
Write a program that displays a rocket countdown sequence starting from a given number. At the end of the countdown, display the words "lift off".

Input format:
A whole number in the range 1 to 100.
Output format:
A series of numbers, each on a separate row, followed by the words "lift off".
Example:
Input:
3
Output:
3
2
1
lift off


# get input:
start = int(input())

# create a list of numbers:
count_down = range(start,0,-1)

# output:
for n in count_down:
    print(n)
print("lift off")



Solar Panels

Introduction
A company manufactures solar panels that measure 0.95m in width and 1.5m in height. These panels can only be installed vertically. They fit seamlessly edge-to-edge on roof sections without requiring gaps between adjacent panels.

Task
Write a program to calculate the maximum number of solar panels that can fit on a rectangular roof section. The program should take the width and height of the roof section as input, and output the maximum number of solar panels that can be installed.

Input format
First line: The width of the roof section in meters
Second line: The height of the roof section in meters
Output format
A number representing the maximum number of solar panels that can be installed. 
Example
Input
5.1
2.0
Output
5


# Get inputs
roof_width = float(input())
roof_depth = float(input())

sp_width = 0.95
sp_length = 1.5

# Laying vertically
num_rows = int(roof_depth / sp_length)
num_columns = int(roof_width / sp_width)

# Produce output
print(num_rows * num_columns)



Counting Letters

Task
Write a program that counts the total number of vowels and consonants used in a sentence. Output the number of vowels then the number of consonants, separated by a space.

Input format
A sentence. The sentence will contain only upper and lowercase letters, spaces and a full-stop.
Output format
The number of vowels followed by the the number of consonants separated by a space.
Example
Input
I love programming.
Output
6 10


# Input sentence provided and remove capitalisation.
sentence = input().lower()

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
vowel_count = 0
consonant_count = 0

for letter in sentence:
    if letter in vowels:
        vowel_count += 1
    if letter in consonants:
        consonant_count += 1

print(vowel_count, consonant_count)



Pig Latin

Introduction
Pig Latin is a language where words are made by modifying English words. The rules are as follows:

If the letter starts with a consonant:
Step 1: Remove the first letter of the word.
Step 2: Add a “-” to the end of the word.
Step 3: Add the letter you removed in step 1 to the end of the word.
Step 4: Add ”ay” to the end of the word. 
If the letter starts with a vowel:
Just add “-yay“ to the end of the word.
Task
Write a program that translates a word into Pig Latin.

Input format
A single English word. The word will only consist of uppercase and lowercase letters.
Output format
The same word in Pig Latin. 
Example 1
Input
Hello
Output
ello-Hay
Example 2
Input
Egg
Output
Egg-yay


# get input
message = input().split()

vowels = "aeiouAEIOU"

for word in message:
    if word[0] not in vowels:
        pig_latin = word[1:] + "-" + word[0] + "ay"
    else:
        pig_latin = word + "-yay"

# output pig-latin
print(pig_latin)
'''

