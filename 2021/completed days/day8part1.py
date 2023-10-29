#60 characters before pipe

f = open("inputday8.txt", "r")

#check each character until i find a bar | 
placeholder = 0
nextchar = ' '
counter = 0
totalcount = 0
nextnextchar = 0

for i in range(200):
    counter =0
    for i in range(61):
        placeholder = f.read(1)
        #print(placeholder)
        nextchar = 'z'
    while nextchar != '\n' and nextchar != '':
        nextchar = f.read(1)
        print('nextchar', nextchar)
        if nextchar != ' ':
            if counter == 2 or counter == 3 or counter == 1 or counter == 6:
                nextnextchar = f.read(1)
                #print('nextnext', nextnextchar)
                if nextnextchar == ' ' or nextnextchar == '\n':
                    totalcount += 1
                    counter = 0
                f.seek(f.tell()-1) 
            counter = counter + 1
        else:
            counter = 0
        print('counter', counter, 'totalcount', totalcount)
