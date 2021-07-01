import string
groups = []


with open("items6") as file:
    record = []
    for line in file.read().split("\n"):
        if line != '':
            for element in line.split(" "):
                record.append(element)

        else:
            groups.append(record)
            record = []
    groups.append(record)

abc = list(string.ascii_lowercase)

sum = 0
for group in groups:
    list = []
    for answer in group:
        for char in answer:
            if char not in list:
                if char in abc:
                    list.append(char)
    length = len(list)
    sum += length

print('Part1: ' + str(sum))


#part2
sum2 = 0
for group in groups:
    list2 = []
    for answer in group:
        for char in answer:
            list2.append(char)
    for a in abc:
        if list2.count(a) == len(group):
            sum2 += 1

print('Part2: ' + str(sum2))


