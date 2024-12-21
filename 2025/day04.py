from itertools import product
from utils import file_to_list

INPUT_FILE_TEST = "inputs/day04.test.in"
INPUT_FILE = "inputs/day04.in"


def part1(filename: str) -> int:
    wordsearch = file_to_list(filename)

    h = len(wordsearch)
    w = len(wordsearch[0])
    orientations = [
        [(i * x, i * y) for i in range(4)]
        for x, y in product((-1, 0, 1), (-1, 0, 1))
        if not (x == y == 0)
    ]

    instances = 0
    for i, j in product(range(h), range(w)):
        for orientation in orientations:
            if not (
                (0 <= i + orientation[-1][0] < h) and (0 <= j + orientation[-1][1] < w)
            ):
                continue
            letters = [wordsearch[i + di][j + dj] for (di, dj) in orientation]
            if letters == ["X", "M", "A", "S"]:
                instances += 1

    return instances


print(part1(INPUT_FILE_TEST))
print(part1(INPUT_FILE))


def part2(filename: str) -> int:
    wordsearch = file_to_list(filename)

    h = len(wordsearch)
    w = len(wordsearch[0])
    star = [(x, y) for x, y in product((-1, 1), (-1, 1))]

    instances = 0
    for i, j in product(range(1, h - 1), range(1, w - 1)):
        if wordsearch[i][j] != "A":
            continue
        letters = [wordsearch[i + di][j + dj] for di, dj in star]
        word1 = letters[0] + "A" + letters[3]
        word2 = letters[1] + "A" + letters[2]

        word1_valid = word1 in ("MAS", "SAM")
        word2_valid = word2 in ("MAS", "SAM")
        if word1_valid and word2_valid:
            instances += 1

    return instances


print(part2(INPUT_FILE_TEST))
print(part2(INPUT_FILE))
