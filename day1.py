# ---- Part 1 ----

def read_file_to_list_of_ints(file):
    ints = []
    with open(file, 'r') as f:
        for row in f:
            ints.append(int(row))
    return ints


def part1(sorted_ints):
    for i, exp in enumerate(sorted_ints):
        for j in range(i + 1, len(sorted_ints)):
            total = exp + sorted_ints[j]
            if total > 2020:
                break;
            elif total == 2020:
                print(exp, '*', sorted_ints[j], '=', exp * sorted_ints[j])


# ---- Part 2 ----

def part2(sorted_ints):
    for i, exp in enumerate(sorted_ints):
        for j in range(i + 1, len(sorted_ints)):
            for k in range(j + 1, len(sorted_ints)):
                total = exp + sorted_ints[j] + sorted_ints[k]
                if total > 2020:
                    break;
                elif total == 2020:
                    print(exp, '*', sorted_ints[j], '*', sorted_ints[k], '=',
                          exp * sorted_ints[j] * sorted_ints[k])


if __name__ == '__main__':
    expense_report = read_file_to_list_of_ints('day1_input.txt')
    expense_report.sort()
    part1(expense_report)
    part2(expense_report)