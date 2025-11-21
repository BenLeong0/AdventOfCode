from collections import defaultdict
from utils import file_to_list

INPUT_FILE_TEST = "inputs/day01.test.in"
INPUT_FILE = "inputs/day01.in"


def part1(filename: str) -> int:
    rows = file_to_list(filename)
    first_els = sorted(int(row.split("   ")[0]) for row in rows)
    second_els = sorted(int(row.split("   ")[1]) for row in rows)

    total = 0
    for x, y in zip(first_els, second_els):
        total += abs(x - y)
    return total


print(part1(INPUT_FILE_TEST))
print(part1(INPUT_FILE))


def part2(filename: str) -> int:
    rows = file_to_list(filename)
    first_els = sorted(int(row.split("   ")[0]) for row in rows)
    second_els = sorted(int(row.split("   ")[1]) for row in rows)

    score_mapping = defaultdict(int)
    for el in second_els:
        score_mapping[el] += 1

    return sum(score_mapping[el] * el for el in first_els)


print(part2(INPUT_FILE_TEST))
print(part2(INPUT_FILE))
