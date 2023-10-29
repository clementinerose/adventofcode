import re

f = open("input7.txt", 'r+')

level, total, counter, dir_size, dir_count = 0,0,0,0,0
dir_name = [['','/']]

line = f.readline().strip('\n')


while True:  
    if not line: break
    # keep track of levels 
    if line[0:4] == "$ cd":
        if line[0:7] == "$ cd ..":
            level -= 1
        elif line[0:6] == "$ cd /":
            level = 0
        else:
            level += 1 
            dir_name.append(line.split("$ cd "))

        line = f.readline().strip('\n')
     

    elif line[0:4] == "$ ls":
        if line[0:4] == "$ cd":
            break 
        line = f.readline().strip("\n") # read next line
        if not line: break
        dir_size = 0 # init directory size to 0

        while line[0] != "$": # while the next line is not the end of dir list
            if line[0:3] != "dir": # if the line is not a dir
                tmp = re.sub(r'\D', '', line) # strip line of anything non-numerical
                dir_size += int(tmp.strip('')) # add result to dir size
            #else:
                #dir_name.append(line.split("dir "))
            line = f.readline().strip("\n")
            if not line: break
        dir_name[dir_count][0] = dir_size
        dir_count += 1

for s in range(len(dir_name)):
    if dir_name[s][0] > 100000:
        total += dir_name[s][0]

print("Grand Total: ", total, dir_name, level)
f.close()

1762286
38506279