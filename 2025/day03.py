import re

INPUT_FILE_TEST = "inputs/day03.test.in"
INPUT_FILE_TEST2 = "inputs/day03.test2.in"
INPUT_FILE = "inputs/day03.in"


def part1(filename: str) -> int:
    MUL_RE = re.compile(r"mul\((\d+),(\d+)\)")
    with open(filename) as f:
        res = MUL_RE.findall(f.read())
    return sum(int(x[0]) * int(x[1]) for x in res)


print(part1(INPUT_FILE_TEST))
print(part1(INPUT_FILE))


def part2(filename: str) -> int:
    MUL_RE = re.compile(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")
    with open(filename) as f:
        res = MUL_RE.findall(f.read())

    total = 0
    active = True
    for x in res:
        if x[2]:
            active = True
        if x[3]:
            active = False
        if x[0] and active:
            total += int(x[0]) * int(x[1])

    return total


print(part2(INPUT_FILE_TEST2))
print(part2(INPUT_FILE))
