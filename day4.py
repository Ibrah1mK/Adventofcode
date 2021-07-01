data = []

with open("data4") as file:
    record = []
    for line in file.read().split("\n"):

        if line != '':
            for element in line.split(" "):
                record.append(element)

        else:
            data.append(record)
            record = []
    data.append(record)

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

validPasswords = 0
for record in data:
    found = [0, 0, 0, 0, 0, 0, 0, 1]

    for element in record:
        sep = element.split(":")
        found[fields.index(sep[0])] += 1

    if 0 not in found:
        validPasswords += 1

print('Part1: ' + str(validPasswords))


# part2
def byr_is_valid(byr):
    if 1920 <= byr <= 2002:
        return True
    return False


def iyr_is_valid(iyr):
    if 2010 <= iyr <= 2020:
        return True
    return False


def eyr_is_valid(eyr):
    if 2020 <= eyr <= 2030:
        return True
    return False


def hgt_is_valid(hgt):
    if 'cm' in hgt:
        cm = hgt.index('c')
        cmheight = int(hgt[:cm])
        if 150 <= cmheight <= 193:
            return True
    if 'in' in hgt:
        inch = hgt.index('i')
        inheight = int(hgt[:inch])
        if 59 <= inheight <= 76:
            return True
    return False


def hcl_is_valid(hcl):
    if '#' in hcl:
        if hcl.index('#') == 0 and len(hcl) == 7:
            for char in hcl[1:]:
                if char in ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    return True
    return False


def ecl_is_valid(ecl):
    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False


def pid_is_valid(pid):
    if len(pid) == 9:
        return True
    return False


correctPasswords = 0
for record in data:
    numtrue = 0

    for element in record:
        sep = element.split(":")

        if sep[0] == 'byr':
            if byr_is_valid(int(sep[1])):
                numtrue += 1

        if sep[0] == 'iyr':
            if iyr_is_valid(int(sep[1])):
                numtrue += 1

        if sep[0] == 'eyr':
            if eyr_is_valid(int(sep[1])):
                numtrue += 1

        if sep[0] == 'hgt':
            if hgt_is_valid(sep[1]):
                numtrue += 1

        if sep[0] == 'hcl':
            if hcl_is_valid(sep[1]):
                numtrue += 1

        if sep[0] == 'ecl':
            if ecl_is_valid(sep[1]):
                numtrue += 1

        if sep[0] == 'pid':
            if pid_is_valid(str(sep[1])):
                numtrue += 1

    if numtrue == 7:
        correctPasswords += 1

print('Part2: ' + str(correctPasswords))
