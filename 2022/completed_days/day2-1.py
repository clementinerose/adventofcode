f = open("input2.txt", "r")

counter = 0
lines= 0

for line in f:
    lines += 1
    if line[0] == 'A' and line[2] == 'Y':
      counter += 8
    elif line[0] == 'B' and line[2] == 'X': #works
      counter += 1
    elif line[0] == 'C' and line[2] == 'Z': #works
      counter += 6
    elif line[0] == 'C' and line[2] == 'X':
      counter += 7
    elif line[0] == 'C' and line[2] == 'Y':
      counter += 2
    elif line[0] == 'A' and line[2] == 'Z':
      counter += 3
    elif line[0] == 'A' and line[2] == 'X':
      counter += 4
    elif line[0] == 'B' and line[2] == 'Z':
      counter += 9
    elif line[0] == 'B' and line[2] == 'Y':
      counter += 5

print(counter, lines)
