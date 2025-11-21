from itertools import product
from utils import file_to_list

INPUT_FILE_TEST = "inputs/day08.test.in"
INPUT_FILE = "inputs/day08.in"


def part1(filename: str) -> int:
    rows = file_to_list(filename)
    map_ = [list(row) for row in rows]
    h, w = len(map_), len(map_[0])
    antinodes = [[False for _ in range(w)] for __ in range(h)]

    for i1, j1 in product(range(h), range(w)):
        frequency1 = map_[i1][j1]
        if frequency1 == ".":
            continue
        for i2, j2 in product(range(h), range(w)):
            frequency2 = map_[i2][j2]
            if (i1, j2) == (i2, j2) or frequency1 != frequency2:
                continue
            antinode_pos_i, antinode_pos_j = (2 * i2 - i1, 2 * j2 - j1)
            if 0 <= antinode_pos_i < h and 0 <= antinode_pos_j < w:
                antinodes[antinode_pos_i][antinode_pos_j] = True

    return sum(sum(row) for row in antinodes)


print(part1(INPUT_FILE_TEST))
print(part1(INPUT_FILE))


def part2(filename: str) -> int:
    rows = file_to_list(filename)
    map_ = [list(row) for row in rows]
    h, w = len(map_), len(map_[0])
    antinodes = [[False for _ in range(w)] for __ in range(h)]

    for i1, j1 in product(range(h), range(w)):
        frequency1 = map_[i1][j1]
        if frequency1 == ".":
            continue
        for i2, j2 in product(range(h), range(w)):
            frequency2 = map_[i2][j2]
            if (i1, j2) == (i2, j2) or frequency1 != frequency2:
                continue

            antinode_pos_i, antinode_pos_j = (i2, j2)
            while 0 <= antinode_pos_i < h and 0 <= antinode_pos_j < w:
                antinodes[antinode_pos_i][antinode_pos_j] = True
                antinode_pos_i, antinode_pos_j = (
                    antinode_pos_i + i2 - i1,
                    antinode_pos_j + j2 - j1,
                )

    return sum(sum(row) for row in antinodes)


print(part2(INPUT_FILE_TEST))
print(part2(INPUT_FILE))
