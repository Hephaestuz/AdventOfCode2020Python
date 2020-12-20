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

# TODO: implement day 4 part 2


if __name__ == '__main__':
    part1()

