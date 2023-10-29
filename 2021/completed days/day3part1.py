#REPLACE 12 WITH WHICHEVER VALUE OF THAT ARRAY YOU WANT TO TEST

# Open the file inputday3.txt for reading only 
arrayfirstvalue = [0] * 2000
array2value = [0] * 2000
array3value = [0] * 2000
array4value = [0] * 2000
array5value = [0] * 2000
array6value = [0] * 2000
array7value = [0] * 2000
array8value = [0] * 2000
array9value = [0] * 2000
array10value = [0] * 2000
array11value = [0] * 2000
array12value = [0] * 2000

i = 0
placeholder= 0 
f = open("inputday3.txt")
#for eachLine in f:

for i in range(1000):
    #print(f.read(12))
    arrayfirstvalue[i] = f.read(1)
    array2value[i] = f.read(1)
    array3value[i] = f.read(1)
    array4value[i] = f.read(1)
    array5value[i] = f.read(1)
    array6value[i] = f.read(1)
    array7value[i] = f.read(1)
    array8value[i] = f.read(1)
    array9value[i] = f.read(1)
    array10value[i] = f.read(1)
    array11value[i] = f.read(1)
    array12value[i] = f.read(1)
    placeholder = f.read(1)

    #print(array2value[i])
    i = i + 1

zerocount = [0] * 13
onecount = [0] * 13

for x in range(1000):
    if array12value[x] == '0':
        zerocount[12] = zerocount[12] + 1
        #print(arrayfirstvalue[i])
    elif array12value[x] == '1':
        onecount[12] = onecount[12] + 1

print('0',zerocount[12])
print('1',onecount[12])

f.close()