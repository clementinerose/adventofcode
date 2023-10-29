f = open("input4.txt", "r")

counter = 0

for line in f:
    elf = line.split(",")

    elf1 = elf[0].split("-")
    elf2 = elf[1].split("-")
    elf2[1] = elf2[1].strip('\n')

    a = int(elf1[0])
    b = int(elf1[1])
    c = int(elf2[0])
    d = int(elf2[1])

     
    if a <= c and b >= d and not d < a:
        counter += 1
        print(line, 1)

    elif c <= a and d >= b and not b < c:
        counter += 1
        print(line, 2) 
    
    
print(counter)