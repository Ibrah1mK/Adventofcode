#part1

with open("items3") as u:
    list = u.readlines()
    list = [line.strip() for line in list]

counttrees = 0
row, col = 0,0

while row+1 < len(list):
    row += 1
    col += 3

    space = list[row][col % len(list[row])] # %, damit col bei Erreichen der max. Länge wieder von vorne beginnt
    if space == '#':
        counttrees += 1

print(counttrees)

#part2
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

total = 1

for slope in slopes:
    counttrees = 0
    row, col = 0,0

    while row+1 < len(list):
        row += slope[1]
        col += slope[0]

        space = list[row][col % len(list[row])] # %, damit col bei Erreichen der max. Länge wieder von vorne beginnt
        if space == '#':
            counttrees += 1

    total *= counttrees

print(total)

