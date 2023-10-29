f = open("inputday9.txt")

input = [' '] * 100
counter = 0

#paste all the file into a two dimensional array 
for i in range(100):
    input[i] = f.readline()

#iterate through all the numbers checking with four loops wether it is bigger 
for i in range(100):
    for j in range(100):
        #top row (pretty sure it works)
        if i == 0 and j > 0 and j != 99:
            if input[0][j] < input[1][j] and input[0][j] < input[0][j + 1] and input[0][j] < input[0][j-1]: 
                counter = counter + 1 + int(input[0][j])
        #normal directions
        elif j != 0 and j != 99 and i != 0 and i != 99:
            if input[i][j] < input[i - 1][j] and input[i][j] < input[i + 1][j] and input[i][j - 1] > input[i][j] and input[i][j] < input[i][j + 1]:
                counter = counter + 1 + int(input[i][j])
        #bottom row
        elif i == 99 and j > 0 and j < 99:
            if input[99][j] < input[98][j] and input[99][j] < input[99][j + 1] and input[99][j] < input[99][j - 1]:
                counter = counter + 1 + int(input[99][j])
        #j == 0 (first column)
        elif j == 0 and i != 0 and i != 99:
            if input[i][j] < input[i - 1][j] and input[i][j] < input[i][j + 1] and input[i][j] < input[i + 1][j]:
                counter = counter + 1 + int(input[i][0])
                print('x')
        #j == 99 (last column)
        elif j == 99 and i != 0 and i != 99:
            if input[i][j] < input[i - 1][j] and input[i][j] < input[i][j - 1] and input[i][j] < input[i + 1][j]:
                counter = counter + 1 + int(input[i][99])
                print(99)

#print counter 
print("counter", counter)