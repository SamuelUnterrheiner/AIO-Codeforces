inputfile = open("rpsin.txt", "r")
outputfile = open("rpsout.txt", "w")

num_rounds = inputfile.readline()
oponent_rock, oponent_paper, oponent_scissors = map(int, inputfile.readline().split())
your_rock, your_paper, your_scissors = map(int, inputfile.readline().split())
score = 0

for i in range(oponent_rock):
    if your_paper > 0:
        oponent_rock -= 1
        your_paper -= 1
        score += 1
    else:
        break

for i in range(oponent_paper):
    if your_scissors > 0:
        oponent_paper -= 1
        your_scissors -= 1
        score += 1
    else:
        break

for i in range(oponent_scissors):
    if your_rock > 0:
        oponent_scissors -= 1
        your_rock -= 1
        score += 1
    else:
        break


for i in range(oponent_rock):
    if your_rock > 0:
        your_rock -= 1
        oponent_rock -= 1
    else:
        break

for i in range(oponent_paper):
    if your_paper > 0:
        your_paper -= 1
        oponent_paper -= 1
    else:
        break

for i in range(oponent_scissors):
    if your_scissors > 0:
        your_scissors -= 1
        oponent_scissors -= 1
    else:
        break

score -= (oponent_rock + oponent_paper + oponent_scissors)

print(score, file = outputfile)