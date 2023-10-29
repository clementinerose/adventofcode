f = open('input6.txt', 'r').read()

found, i = False, 0

while found == False:
    if (len(set(f[i:i+4])) == 4) == True:
        print(f[i:i+4], i+4)
        found = True
    i += 1