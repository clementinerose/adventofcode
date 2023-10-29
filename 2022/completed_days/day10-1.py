f = open("input10.txt")

output, cycle = 0, 0
X = 1

for line in f:
    if line[0:4] == 'noop': cycle += 1
    elif line[0:4] == 'addx':
        for i in range(2):
            cycle += 1
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                output += X * cycle
        add = line.strip('addx').strip('\n').strip()
        X += int(add)
        
print(output)