f = open("input5.txt")

#first element is bottom of the stack
stacks = [[], ["Z", "N"], ["M", "C", "D"], ["P"]]

for i in range(10):
    next(f)
for line in f:

    #init quantity, start stack and end stack 
    if len(line) == 19:
        qty, start_stack, end_stack = int(line[5]), int(line[12]), int(line[17])
    elif len(line) == 18:
        qty, start_stack, end_stack = int(line[5]), int(line[12]), int(line[17])
    elif len(line) == 20:
        start_stack, end_stack = int(line[13]), int(line[18])
        qty = (int(line[5])*10) + int(line[6])

    x = 0
    buffer = []

    for e in range(0,qty):
        last = len(stacks[start_stack]) - 1
        print(1, last, qty, buffer, stacks, stacks[start_stack])
        buffer.append(stacks[start_stack][last])
        stacks[start_stack].pop(last)
        x += 1
        print(1, last, qty, buffer, stacks, stacks[start_stack])

    for j in range(0, len(buffer)):
        stacks[end_stack].append(buffer[j])
        print(2, buffer, stacks)

    
for k in range(1, 4):
    print(stacks[k][-1])
    print(stacks)
