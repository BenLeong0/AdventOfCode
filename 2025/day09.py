from typing import Optional
from utils import file_to_list

INPUT_FILE_TEST = "inputs/day09.test.in"
INPUT_FILE = "inputs/day09.in"


def part1(filename: str) -> int:
    rows = file_to_list(filename)

    files: list[Optional[int]] = []
    curr_id = 0
    for i, n in enumerate(rows[0]):
        if i % 2 == 0:
            files += [curr_id] * int(n)
            curr_id += 1
        else:
            files += [None] * int(n)

    p1, p2 = 0, len(files) - 1

    while p1 < p2:
        if files[p1] is not None:
            p1 += 1
        elif files[p2] is None:
            p2 -= 1
        else:
            files[p1], files[p2] = files[p2], files[p1]

    return sum(i * n for (i, n) in enumerate(files) if n is not None)


print(part1(INPUT_FILE_TEST))
print(part1(INPUT_FILE))


def part2(filename: str) -> int:
    rows = file_to_list(filename)

    files: list[tuple[Optional[int], int]] = []
    curr_id = 0
    for i, n in enumerate(rows[0]):
        if i % 2 == 0:
            files.append((curr_id, int(n)))
            curr_id += 1
        else:
            files.append((None, int(n)))

    p2 = len(files) - 1

    while p2 > 0:
        if files[p2][0] is None:
            p2 -= 1
            continue
        p1 = 0
        while p1 < p2:
            if files[p1][0] is not None:
                p1 += 1
                continue
            p1size, p2size = files[p1][1], files[p2][1]
            if p1size < p2size:
                p1 += 1
                continue
            files = [
                *files[:p1],
                files[p2],
                (None, p1size - p2size),
                *files[p1 + 1 : p2],
                (None, p2size),
                *files[p2 + 1 :],
            ]
            break
        p2 -= 1

    checksum_arr: list[Optional[int]] = []
    for n, i in files:
        checksum_arr += [n] * i
    return sum(i * n for (i, n) in enumerate(checksum_arr) if n is not None)


print(part2(INPUT_FILE_TEST))
print(part2(INPUT_FILE))
