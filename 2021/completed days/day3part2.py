f = open("inputday3.txt")

line = []
zerocount = [0] * 13
onecount = [0] * 13
most = [''] * 13

todel = [0] * 12

for i in range(1, 1001):
    line.append(f.readline())

for z in range(0, 13):
    #for each line of input
    for i in range(0, len(line)):
        #for each character 
        #COUNT UP ZERO'S AND ONE'S 
        if line[i][z] == '0':
            zerocount[z] += 1
        else:
            onecount[z] += 1
            #print(line[i], z, 1)
    
    if zerocount[z] < onecount[z] or zerocount[z] == onecount[z]:
        most[z] = '1'
    else:
        most[z] = '0'

    print("most", most[z])
    
    for a in range(1):
        while a < len(line):
            if line[a][z] is not most[z]:
                del line[a]
            else:
                a += 1

    if len(line) == 1:
        break

print(line[0])
f.close()