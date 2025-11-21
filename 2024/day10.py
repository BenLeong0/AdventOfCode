from itertools import product
from utils import file_to_list

INPUT_FILE_TEST = "inputs/day10.test.in"
INPUT_FILE = "inputs/day10.in"


Pos = tuple[int, int]


def part1(filename: str) -> int:
    rows = file_to_list(filename)
    map_ = [[int(n) for n in row] for row in rows]
    h, w = len(map_), len(map_[0])

    score = 0
    for pos in product(range(h), range(w)):
        if map_[pos[0]][pos[1]] == 0:
            seen: set[Pos] = set()
            score += _get_score(map_, pos, seen)
    return score


def _get_score(map_: list[list[int]], pos: Pos, seen: set[Pos]) -> int:
    if pos in seen:
        return 0
    seen.add(pos)

    height = map_[pos[0]][pos[1]]
    if height == 9:
        return 1

    score = 0
    for new_pos in _get_next_positions(pos):
        if not (0 <= new_pos[0] < len(map_) and 0 <= new_pos[1] < len(map_[0])):
            continue
        new_height = map_[new_pos[0]][new_pos[1]]
        if new_height == height + 1:
            score += _get_score(map_, new_pos, seen)
    return score


def _get_next_positions(curr_pos: Pos) -> list[Pos]:
    os = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    return [(curr_pos[0] + o[0], curr_pos[1] + o[1]) for o in os]


print(part1(INPUT_FILE_TEST))
print(part1(INPUT_FILE))


def part2(filename: str) -> int:
    rows = file_to_list(filename)
    map_ = [[int(n) for n in row] for row in rows]
    h, w = len(map_), len(map_[0])

    score = 0
    for pos in product(range(h), range(w)):
        if map_[pos[0]][pos[1]] == 0:
            score += _get_rating(map_, pos)
    return score


def _get_rating(map_: list[list[int]], pos: Pos) -> int:
    height = map_[pos[0]][pos[1]]
    if height == 9:
        return 1

    score = 0
    for new_pos in _get_next_positions(pos):
        if not (0 <= new_pos[0] < len(map_) and 0 <= new_pos[1] < len(map_[0])):
            continue
        new_height = map_[new_pos[0]][new_pos[1]]
        if new_height == height + 1:
            score += _get_rating(map_, new_pos)
    return score


print(part2(INPUT_FILE_TEST))
print(part2(INPUT_FILE))
