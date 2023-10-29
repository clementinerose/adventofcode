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

totalsb = 0
totalcb = 0
totalcr = 0
totalpr = 0

# cycle through each char of each line
for i in range(94):
    squarebracket = 0
    curlybrace = 0
    crocodile = 0
    parentheses = 0
    for j in range(len(input[i])):
        # test if elif if each character corresponds to one of the 8 chars
        if input[i][j] == '[':
            squarebracket += 1
        elif input[i][j] == '{':
            curlybrace += 1
        elif input[i][j] == '<':
            crocodile += 1
        elif input[i][j] == '(':
            parentheses += 1
        elif input[i][j] == ']':
            squarebracket -= 1
            if squarebracket < 1:
                totalsb += 1
                break
        elif input[i][j] == '}':
            curlybrace -= 1
            if curlybrace < 1:
                totalcb += 1
                break
        if input[i][j] == '>':
            crocodile -= 1
            if crocodile < 1:
                totalcr += 1
                break
        if input[i][j] == ')':
            parentheses -= 1
            if parentheses < 1:
                totalpr += 1
                break
        
total = 0

#): 3 points.
for i in range(totalpr):
    total += 3
#]: 57 points.
for i in range(totalsb):
    total += 57
#}: 1197 points.
for i in range(totalcb):
    total += 1197
#>: 25137 points.
for i in range(totalcr):
    total += 25137

print("[]]", totalsb, "{}", totalcb, "<>", totalcr, "()", totalpr)
print(total)

# if it does and it's an opening char then add one to that char character 
# if it's a closing char, check if the corresponding opening counter 
# has a number > 10, if it does, remove one from the counter and move to next char
# if the counter is 0, then add one to that specific error counter and go to new line 
# once at the end of the file, multiply the number of error counts 
# (should total to number of lines if not mistaken?) 
# by the corresponding value, add them all together and print 