f = open("input3.txt", "r")

counter = 0
same = ""
it = 0

for line in f:
    same = ""
    # get line length 
    length = len(line.strip()) 

    # get half of that
    middle = length // 2

    line = line.strip()

    #find similarity
    for i in range(0, middle):
        for j in range(0, middle):
            if line[i] == line[middle+j]:
                same = line[i]
                it += 1
                
            if same != "":
                break

    # isupper() if True, add 26 to counter
    if same.isupper() == True:
        counter += 26
        counter += ord(same) - 64
    else:
        counter += ord(same.strip()) - 96
    
print(counter)