with open("data7") as file:
    data = file.readlines()
    data = [line.strip() for line in data]


sg = 'shiny gold'
bagscontainsg = []

#Ermittlung aller bags, die 'shiny gold' bags direkt beinhalten
for line in data:
    bag = line[:line.index(' bags')]
    if sg not in bag and sg in line:
        bagscontainsg.append(bag)

#Ermittlung aller bags, die 'shiny gold' bags indirekt beinhalten
i=0
t=0
while t < len(bagscontainsg):
    t = len(bagscontainsg)
    for line in data:
        bag = line[:line.index(' bags')]
        for b in bagscontainsg:
            if (bag not in bagscontainsg) and (b in line):
                bagscontainsg.append(bag)
print('Part1: ' + str(len(bagscontainsg)))

#part2


def count_bags(color):
    s = ''
    for line in data:
        if line[:line.index(' bags')] == color:
            s = line

    if 'no' in s:
        return 1

    s = s[s.index('contain')+8:].split()

    total = 0
    i = 0
    origin_color = color

    while i < len(s):
         count = int(s[i])
         color = s[i+1] + ' ' + s[i+2]
         total += count * count_bags(color)
         i += 4

    if origin_color == 'shiny gold':
        return total
    return total + 1


count = count_bags('shiny gold')
print('Part2: ' + str(count))





