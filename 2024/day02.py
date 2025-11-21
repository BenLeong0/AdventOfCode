from utils import file_to_list

INPUT_FILE_TEST = "inputs/day02.test.in"
INPUT_FILE = "inputs/day02.in"


def part1(filename: str) -> int:
    rows = file_to_list(filename)

    num_safe = 0
    for row in rows:
        report = [int(x) for x in row.split(" ")]
        increasing = report[1] > report[0]
        if all(
            (
                1 <= report[i + 1] - report[i] <= 3
                if increasing
                else -3 <= report[i + 1] - report[i] <= -1
            )
            for i in range(len(report) - 1)
        ):
            num_safe += 1

    return num_safe


print(part1(INPUT_FILE_TEST))
print(part1(INPUT_FILE))


def part2(filename: str) -> int:
    rows = file_to_list(filename)

    num_safe = 0
    for row in rows:
        report = [int(x) for x in row.split(" ")]
        if p2_is_safe(report):
            num_safe += 1

    return num_safe


def p2_is_safe(report: list[int], already_dampened: bool = False):
    increasing = report[1] > report[0]
    for i in range(len(report) - 1):
        safe = (
            1 <= report[i + 1] - report[i] <= 3
            if increasing
            else -3 <= report[i + 1] - report[i] <= -1
        )
        if safe:
            continue
        if already_dampened:
            return False
        if i == len(report) - 1:
            return True
        return (
            p2_is_safe(report[:i] + report[i + 1 :], True)
            or p2_is_safe(report[: i + 1] + report[i + 2 :], True)
            or p2_is_safe(report[1:], True)
            or p2_is_safe(report[:1] + report[2:], True)
        )
    return True


print(part2(INPUT_FILE_TEST))
print(part2(INPUT_FILE))
