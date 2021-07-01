with open("data7") as file:
    data = file.readlines()
    data = [line.strip() for line in data]


sg = 'shiny gold'
bagscontainsg = []

for line in data:
    bag = line[:line.index(' bags')]
    if sg not in bag and sg in line:
        bagscontainsg.append(bag)

for line in data:
    bag = line[:line.index(' bags')]
    for b in bagscontainsg:
        if (bag not in bagscontainsg) and (b in line):#sucht in der line nur bis zum 1. Komma?
            bagscontainsg.append(bag)

print('Part1: ' + str(len(bagscontainsg)))













