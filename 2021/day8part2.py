#60 characters before pipe
f = open("inputday8.txt", "r")

line = [''] * 200
optioncount = [0] * 7
total = 0

for x in range(200):
    line[x] = f.readline()

#for each line in f
for i in range(len(line)):
    #for each 60 first chars
    for j in range(58):
        #for the 7 different options 
        if line[i][j] == 'a': optioncount[0] += 1
        if line[i][j] == 'b': optioncount[1] += 1
        if line[i][j] == 'c': optioncount[2] += 1
        if line[i][j] == 'd': optioncount[3] += 1
        if line[i][j] == 'e': optioncount[4] += 1
        if line[i][j] == 'f': optioncount[5] += 1
        if line[i][j] == 'g': optioncount[6] += 1
    #for each digit after bar
    x = 0
    digitsum = 0
    string = ['']
    print(i)
    while line[i][x] != '\n':
        while line[i][x] != ' ':
            #add up the sum of the digit 
            if line[i][j] == 'a': digitsum += optioncount[0]
            if line[i][j] == 'b': digitsum += optioncount[1]
            if line[i][j] == 'c': digitsum += optioncount[2]
            if line[i][j] == 'd': digitsum += optioncount[3]
            if line[i][j] == 'e': digitsum += optioncount[4]
            if line[i][j] == 'f': digitsum += optioncount[5]
            if line[i][j] == 'g': digitsum += optioncount[6]
            #compare that to the sums for all the digits
            if line[i][x+1] == ' ':
                if digitsum == 17: string = string + '1'
                if digitsum == 34: string = string + '2'
                if digitsum == 39: string = string + '3'
                if digitsum == 30: string = string + '4'
                if digitsum == 37: string = string + '5'
                if digitsum == 41: string = string + '6'
                if digitsum == 25: string = string + '7'
                if digitsum == 49: string = string + '8'
                if digitsum == 45: string = string + '9'
                if digitsum == 42: string = string + '0'
    total += int(string)
    print(i)
print(total)