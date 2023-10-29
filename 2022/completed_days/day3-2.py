f = open("input3.txt", "r")

counter = 0
same = ""

for i in range(100):
    line1 = f.readline().strip()
    line2 = f.readline().strip()
    line3 = f.readline().strip()

    same = ""

    #find similarity
    for k in range(len(line1)):
        for j in range(len(line2)):
            for x in range(len(line3)):
                if line1[k] == line2[j] == line3[x]:
                    same = line1[k]              
                if same != "":
                    break

    # isupper() if True, add 26 to counter
    if same.isupper() == True:
        counter += 26
        counter += ord(same) - 64
    else:
        counter += ord(same.strip()) - 96
    
print(counter)