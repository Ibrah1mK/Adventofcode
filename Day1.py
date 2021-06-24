list = []
with open("numbers") as u:
    list = u.readlines()

nums = [int(line.strip()) for line in list]

print(list)
print(nums)

for i in nums:
    for j in nums:
        if i>1000 and i + j == 2020:
            print(i*j)
            print(i, j)

for i in nums:
    for j in nums:
        for k in nums:
            if i<1000 and j<500 and i + j + k == 2020:
                print(i*j*k)


