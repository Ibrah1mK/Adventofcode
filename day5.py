data = []
seatIDlist = []

with open("data5") as file:
    record = []
    for line in file.read().split("\n"):
        data.append((line))

for passport in data:
    minrow, maxrow = 0, 127
    mincolumn, maxcolumn= 0, 7
    for i in passport:
        if i == 'F':
            maxrow = (minrow+maxrow)//2

        if i == 'B':
            minrow = (minrow+maxrow)//2 +1


        if i == 'L':
            maxcolumn = (maxcolumn+mincolumn)//2

        if i == 'R':
            mincolumn = (maxcolumn+mincolumn)//2 +1

    seatID = maxrow*8 + maxcolumn
    seatIDlist.append(seatID)

print('Part1: ' + str(max(seatIDlist)))

#part2

minid = min(seatIDlist)
for id in seatIDlist:
    if id > minid:
        if id+1 in seatIDlist and id-1 not in seatIDlist:
            print('Part2: ' + str(id-1))