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

    print(a, b, c, d)
     
    if a <= c and d <= b:
        counter += 1
        print(1)

    elif c <= a and b <= d:
        counter += 1
        print(2)

    elif b == c or c == a or b == d or a == d:
        counter += 1
        print(3)

    elif a < c and b < d and b > c:
        counter += 1
        print(4)

    elif c < a and d < b and d > a:
        counter += 1
        print(5)

print(counter)