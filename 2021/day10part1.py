# open file in two dimensional array
f = open("inputday10.txt")
input = [' '] * 94

for i in range(94):
    input[i] = f.readline() 

#counters
squarebracket = 0
curlybrace = 0
crocodile = 0
parentheses = 0

for i in range(94):
    linelength = len(input[i])
    for j in range(linelength):
        if input[i][j] == 
