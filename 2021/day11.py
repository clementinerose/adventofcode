#open the file up as a two dimensional array 
f = open("inputday11.txt")

w, h = 10, 10
data = [[0 for x in range(w)] for y in range(h)]

file = [''] * 10
for i in range(10):
    file[i] = f.readline()

for x in range(10):
    for y in range(10):
        data[x][y] = int(file[x][y])

counter = 0

)


#cycle thru if value > 9 

#then it adds one to flash counter 
#set value to 0
#increase values of surrounding values by 1 and restart to process
#repeat 100 times 
#print counter
print(counter) 