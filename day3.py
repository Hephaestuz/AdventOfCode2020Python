# ---- Part 1 ----

def read_file(file):
    with open(file, 'r') as f:
        for row in f:
            yield row.strip()


def part1():
    x = 0
    step_right = 3
    count = 0
    for row in read_file('day3_input.txt'):
        if row[x] == '#':
            count += 1
        x += step_right
        x = x % len(row)
    print(count)


# ---- Part 1 ----

def tree_in_path(step_right, step_down):
    x = 0
    count = 0
    for i, row in enumerate(read_file('day3_input.txt')):
        if i % step_down == 0:
            if row[x] == '#':
                count += 1
            x += step_right
        x = x % len(row)
    return count


def part2():
    prod = 1
    for a, b in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        tree_count = tree_in_path(a, b)
        prod *= tree_count
    print(prod)


if __name__ == '__main__':
    part1()
    part2()

