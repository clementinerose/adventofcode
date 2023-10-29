f = open("inputday9.txt")

input = [' '] * 100
counter = 0

#paste all the file into a two dimensional array 
for i in range(100):
    input[i] = f.readline()

