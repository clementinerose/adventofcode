f = open("inputday2.txt")

line = '0'
horizontal = 0
depth = 0
#aim = 0

for i in range(1000):
    line = f.readline()
    if line[0] == 'u':
        depth -= int(line[3])
        #aim -= int(line[3])
    elif line[0] == 'd':
        depth += int(line[5])
        #aim += int(line[5])
    elif line[0] == 'f':
        horizontal += int(line[8])
        #depth += (aim * int(line[8]))

print(horizontal, depth)