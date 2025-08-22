num_of_testcases = int(input())
for i in range(num_of_testcases):
    word1, word2 = input().split()
    print(word2[0]+word1[1]+word1[2], word1[0]+word2[1]+word2[2]) 