# ruff: noqa: E731

from utils import file_to_list

INPUT_FILE_TEST = "inputs/day02.test.in"
INPUT_FILE = "inputs/day02.in"


def part1(filename: str) -> int:
    rows = file_to_list(filename)[0].split(",")

    sum = 0
    for row in rows:
        [lower, upper] = row.split("-")
        for i in range(int(lower), int(upper) + 1):
            stri = str(i)
            if stri[: len(stri) // 2] * 2 == stri:
                sum += i

    return sum


part1ol = lambda filename: sum(
    sum(
        a
        for a in range(int(s[0]), int(s[1]) + 1)
        if str(a)[: len(str(a)) // 2] * 2 == str(a)
    )
    for y in [x for x in open(filename).readline().split(",")]
    if (s := y.split("-"))
)

# print(part1(INPUT_FILE_TEST))
# print(part1ol(INPUT_FILE_TEST))
# print(part1(INPUT_FILE))
# print(part1ol(INPUT_FILE))


def part2(filename: str) -> int:
    rows = file_to_list(filename)[0].split(",")

    sum = 0
    for row in rows:
        [lower, upper] = row.split("-")
        for i in range(int(lower), int(upper) + 1):
            stri = str(i)
            if any(
                stri[: len(stri) // div] * div == stri
                for div in range(2, len(stri) + 1)
            ):
                sum += i

    return sum


part2ol = lambda filename: sum(
    sum(
        a
        for a in range(int(s[0]), int(s[1]) + 1)
        if (sa := str(a))
        and any(sa[: len(sa) // div] * div == sa for div in range(2, len(sa) + 1))
    )
    for y in [x for x in open(filename).readline().split(",")]
    if (s := y.split("-"))
)


print(part2(INPUT_FILE_TEST))
print(part2ol(INPUT_FILE_TEST))
print(part2(INPUT_FILE))
print(part2ol(INPUT_FILE))
