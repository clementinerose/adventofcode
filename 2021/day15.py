import random as random

f = open("inputday15.txt", "r")

risk = [0] * 100
variables = [''] * 10 

for x in range(10):
    variables[x] = f.readline()

x = 0
y = 0

for r in range(100):
    while x != 9 and y != 9:
        n = random.randint(0,1)
        if int(variables[x][y+1]) < int(variables[x][y]): 
            print(variables[x][y], variables[x][y+1])
            risk += int(variables[x][y+1])
            x -= 1
        else: 
            risk += int(variables[x][y])
            y -= 1
        x += 1
        y += 1

print(risk)