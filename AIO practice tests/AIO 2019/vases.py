inputfile = open("vasesin.txt", "r")
outputfile = open("vasesout.txt", "w")
vaseA, vaseB, vaseC = 1, 2, 3
num_flowers = int(inputfile.readline() - 6)
if num_flowers >= 0:
    vaseC +=num_flowers
    print(vaseA, vaseB, vaseC, file = outputfile)
else:
    print("0 0 0", file = outputfile)