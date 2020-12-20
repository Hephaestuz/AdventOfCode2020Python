# ---- Part 1 ----


def part1(file):
    count = 0
    with open(file, 'r') as f:
        for row in f:
            rule, password = row.strip().split(':')
            min_max, letter = rule.split()
            mn, mx = min_max.split('-')
            c = password.count(letter)
            if int(mn) <= c <= int(mx):
                count += 1
    print(count)


# ---- Part 2 ----

def part2(file):
    count = 0
    with open(file, 'r') as f:
        for row in f:
            rule, password = row.strip().split(':')
            first_second, letter = rule.split()
            first, second = first_second.split('-')
            a = password[int(first)] == letter
            b = password[int(second)] == letter
            if (a and not b) or (b and not a):
                count += 1
    print(count)


if __name__ == '__main__':
    part1('day2_input.txt')
    part2('day2_input.txt')