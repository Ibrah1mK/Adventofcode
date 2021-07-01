with open("data2") as file:
    data = file.readlines()
    data = [line.strip() for line in data]

data = list(data)

valid = 0
for row in data:
    key, password = row.split(': ')
    i = key.index('-')
    intervall, char = key.split(' ')
    lowest = int(intervall[:i])
    highest = int(intervall[i+1:])

    count= 0
    for p in password:

        if char == p:
            count += 1

    if lowest <= count <= highest:
        valid += 1

print('Part1: ' + str(valid))

#part2

valid = 0
for row in data:
    key, password = row.split(': ')
    i = key.index('-')
    intervall, char = key.split(' ')
    pos1 = int(intervall[:i])
    pos2 = int(intervall[i+1:])

    first = password[pos1-1] == char
    second = password[pos2-1] == char

    if (first and not second) or (second and not first):
        valid += 1

print('Part2: ' + str(valid))










