f = open("input10.txt")

crt_position = 0
X = 1
output = []

for line in f:
    if line[0:4] == 'noop': 
        if crt_position == X or crt_position == X -1 or crt_position == X +1:
            output.append("#")
            crt_position += 1
        else:
            output.append(".")
            crt_position += 1
        if crt_position == 40 or crt_position == 80 or crt_position == 120 or crt_position == 160 or crt_position == 200 or crt_position == 240:
                print(''.join(output))
                output = []
    elif line[0:4] == 'addx':
        for i in range(2):
            if crt_position == X or crt_position == X -1 or crt_position == X +1:
                output.append("#")
            else: output.append(".")
            crt_position += 1
            if crt_position == 40 or crt_position == 80 or crt_position == 120 or crt_position == 160 or crt_position == 200 or crt_position == 240:
                print(''.join(output))
                output = []
                crt_position = 0
        add = line.strip('addx').strip('\n').strip()
        X += int(add)