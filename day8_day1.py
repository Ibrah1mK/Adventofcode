with open("data8") as file:
    data = file.readlines()
    data = [line.strip() for line in data]

data = list(data)
acc = 0
line = 0
instructions = []

while line not in instructions:
    instructions.append(line)

    i = data[line]
    i.split()
    a = i[:i.index(' ')]
    b = int(i[i.index(' '):])
    if a == 'acc':
        acc += b
        line += 1
    if a == 'jmp':
        if line == len((data)):
            break
        else: line += b
    if a == 'nop':
        if b+line == len((data)):
            line += b
        else: line += 1

print('Part1: ' + str(acc))





