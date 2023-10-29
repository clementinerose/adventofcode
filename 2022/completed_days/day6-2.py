f = open('input6.txt', 'r').read()

found, i = False, 0

while found == False:
    if (len(set(f[i:i+14])) == 14) == True:
        print(f[i:i+14], i+14)
        found = True
    i += 1