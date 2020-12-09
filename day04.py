passports = []

with open('inputs/day04input', 'r') as f:
    current_passport = {}
    while True:
        line = f.readline()
        if not line:
            if current_passport:
                passports.append(current_passport)
            break
        elif line == "\n":
            passports.append(current_passport)
            current_passport = {}
            continue

        for field in line[:-1].split(' '):
            current_passport[field.split(":")[0]] = field.split(":")[1]


def check_valid(passport):
    for field in ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']:
        if field not in passport.keys():
            return False

    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return False

    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return False

    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return False

    if passport['hgt'][-2:] == 'cm':
        if int(passport['hgt'][:-2]) < 150 or int(passport['hgt'][:-2]) > 193:
            return False
    elif passport['hgt'][-2:] == 'in':
        if int(passport['hgt'][:-2]) < 59 or int(passport['hgt'][:-2]) > 76:
            return False
    else:
        return False

    if passport['hcl'][0] != '#' or len(passport['hcl']) != 7:
        return False
    for i in range(1, 7):
        if passport['hcl'][i] not in ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']:
            return False

    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if (not passport['pid'].isnumeric()) or (len(passport['pid']) != 9):
        return False

    return True


counter = 0

for passport in passports:
    if check_valid(passport):
        counter += 1

print('There are', counter, 'valid passports.')
