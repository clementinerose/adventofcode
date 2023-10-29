#import numpy as np

f = open("inputday4.txt")
bingolots = [74,79,46,2,19,27,31,90,21,83,94,77,0,29,38,72,42,23,6,62,45,95,41,55,93,69,39,17,12,1,20,53,49,71,61,13,88,25,87,26,50,58,28,51,89,64,3,80,36,65,57,92,52,86,98,78,9,33,44,63,16,34,97,60,40,66,75,4,7,84,22,43,11,85,91,32,48,14,18,76,8,47,24,81,35,30,82,67,37,70,15,5,73,59,54,68,56,96,99,10]

w, h, q = 5, 5, 100
data = [[[0 for x in range(w)] for y in range(h)] for z in range(q)]

file = [''] * 599
for i in range(599):
    file[i] = f.readline()

for w in range(100):
    for x in range(0, 6):
        iterate = 0
        for y in range(0, 13):
            d = x
            if d % 5 != 0 or d == 0:
                if file[x + (w * 6)][y] != ' ' and file[x + (w * 6)][y+1] != (' ' or '\n' or None):
                    data[w][x][iterate] = int(file[x + (w * 6)][y]) * 10 + int(file[x + (w * 6)][y+1])
                    iterate += 1
                elif file[x + (w * 6)][y] == ' ' and y == 0:
                    data[w][x][iterate] = int(file[x + (w * 6)][y+1])
                    iterate += 1
                elif file[x + (w * 6)][y] == ' ':
                    print(y)
                    data[w][x][iterate] = int(file[x + (w * 6)][y+ 1])
                    iterate += 1
            else:
                break

nowinner = False

for i in range(len(bingolots)):
    if nowinner == False:
        for a in range(100):
            for b in range(5):
                for c in range(5):
                    if data[a][b][c] == bingolots[i]:
                        data[a][b][c] = 100

        for d in range(100):
            for e in range(5):
                if data[d][e][0] == 100 and data[d][e][1] == 100 and data[d][e][2] == 100 and data[d][e][3] == 100 and data[d][e][4] == 100 or data[d][0][e] == 100 and data[d][1][e] == 100 and data[d][2][e] == 100 and data[d][3][e] == 100 and data[d][4][e] == 100:
                    print('Array', d, bingolots[i])
                    print(data[d])
                    total = 0
                    for f in range(5):
                        for g in range(5):
                            if data[d][f][g] != 100:
                                total += data[d][f][g]
                    print(total * bingolots[i], total)
                    nowinner = True
    
    if nowinner == True: 
        break


# Go through the entire array and compare each variable to bingolots i
