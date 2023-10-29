f = open("input1.txt")

output = [0]
counter = 0

for line in f:
    if line == '\n':
        counter += 1 
        output.append(0)
    if line.strip():
        output[counter] += int(line)

#sort function from highest to lowest
output.sort(reverse=True)

#calculate top 3 sum 
sum = output[0] + output[1] + output[2]
print(sum)