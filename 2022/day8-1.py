f = open("input8.txt", 'r+')
trees = f.read().split('\n')

counter = 0

for line in range(1, len(trees)):
    for char in range (1, len(trees[0])):
        found = True
        # if the tree in question is bigger than the tree above it and the tree to the right 
        while found == True:
            for z in range(line):
                if trees[line - z][char] < trees[line][char]: # above
                    counter += 1
                    found = False                
                    print(trees[line][char])
                if found == False:
                    break
            if found == False:
                break
            for s in range(len(trees) - line): # below
                if trees[line + s][char] < trees[line][char]:
                    counter+=1
                    found = False
                if found == False:
                    break
            if found == False:
                break
            for k in range(char): # to the right
                if trees[line][char - k] < trees[line][char]:
                    counter+=1
                    found = False
                if found == False:
                    break
            if found == False:
                break
            for d in range(len(trees[0]) - char):
                if trees[line][char + d] < trees[line][char]:
                    counter+= 1
                    found = False
                if found == False:
                    break
            if found == False:
                break

print(counter)