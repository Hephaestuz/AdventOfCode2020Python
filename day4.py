import re


# ---- Part 1 ----

def read_passport(file):
    with open(file, 'r') as f:
        new_passport = False
        r = ""
        for row in f:
            if new_passport:
                new_passport = False
                r = ""
            if row == '\n':
                new_passport = True
                yield r
            else:
                r += " " + row.strip()
        yield r


def validate_passport(passport_details):
    details = {}
    for d in passport_details.split():
        field = d.split(':')
        details[field[0]] = field[1]
    for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
        if field not in details.keys():
            return False
    return True


def part1():
    count = 0
    for row in read_passport('day4_input.txt'):
        count += 1 if validate_passport(row) else 0
    print(count)


# ---- Part 2 ----

def validate_min_max(value, mn, mx):
    return mn <= int(value) <= mx


def validate_byr(value):
    return validate_min_max(value, 1920, 2002)


def validate_iyr(value):
    return validate_min_max(value, 2010, 2020)


def validate_eyr(value):
    return validate_min_max(value, 2020, 2030)


def validate_hgt(value):
    if 'cm' in value:
        return validate_min_max(int(value[:value.index('cm')]), 150, 193)
    if 'in' in value:
        return validate_min_max(int(value[:value.index('in')]), 59, 76)


def validate_hcl(value):
    x = re.search('#[0-9|a-f]{6}$', value)
    if x:
        return True
    else:
        return False


def validate_ecl(value):
    return value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')



def validate_pid(value):
    x = re.search('^[0-9]{9}$', value)
    if x:
        return True
    else:
        return False


def strict_validate_passport(passport_details):
    details = {}
    for d in passport_details.split():
        field = d.split(':')
        details[field[0]] = field[1]
    for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
        if field not in details.keys():
            return False
    if not validate_byr(details['byr']):
        return False
    if not validate_iyr(details['iyr']):
        return False
    if not validate_eyr(details['eyr']):
        return False
    if not validate_hgt(details['hgt']):
        return False
    if not validate_hcl(details['hcl']):
        return False
    if not validate_ecl(details['ecl']):
        return False
    if not validate_pid(details['pid']):
        return False
    return True


def part2():
    count = 0
    for row in read_passport('day4_input.txt'):
        count += 1 if strict_validate_passport(row) else 0
    print(count)


if __name__ == '__main__':
    part1()
    part2()

