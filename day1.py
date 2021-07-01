with open("data1") as u:
    list = u.readlines()

nums = [int(line.strip()) for line in list]

for i in nums:
    for j in nums:
        if i > 1000 and i + j == 2020:
            print('Part1: ' + str(i*j))

for i in nums:
    for j in nums:
        for k in nums:
            if i<1000 and j<500 and i + j + k == 2020:
                print('Part2: ' + str(i*j*k))
