import copy
from itertools import product
from typing import Literal
from utils import file_to_list

INPUT_FILE_TEST = "inputs/day06.test.in"
INPUT_FILE = "inputs/day06.in"

Direction = Literal["^", "<", ">", "v"]


def part1(filename: str) -> int:
    rows = file_to_list(filename)
    map_ = [list(x) for x in rows]

    h, w = len(map_), len(map_[0])

    def in_bounds(pos: tuple[int, int]) -> bool:
        return 0 <= pos[0] < h and 0 <= pos[1] < w

    curr_pos, curr_dir = _get_curr_pos_and_dir(map_)
    while in_bounds(curr_pos):
        pos_change = _get_pos_change(curr_dir)
        new_pos = (curr_pos[0] + pos_change[0], curr_pos[1] + pos_change[1])
        if in_bounds(new_pos) and map_[new_pos[0]][new_pos[1]] == "#":
            curr_dir = _rotate_dir(curr_dir)
        else:
            map_[curr_pos[0]][curr_pos[1]] = "X"
            curr_pos = new_pos

    return sum(row.count("X") for row in map_)


def _get_curr_pos_and_dir(map_: list[list[str]]) -> tuple[tuple[int, int], Direction]:
    for i, row in enumerate(map_):
        for j, pos in enumerate(row):
            if pos in ("^", "<", ">", "v"):
                return (i, j), pos
    raise ValueError("Guard not found")


def _get_pos_change(dir: Direction) -> tuple[int, int]:
    match dir:
        case "<":
            return (0, -1)
        case ">":
            return (0, 1)
        case "^":
            return (-1, 0)
        case "v":
            return (1, 0)


def _rotate_dir(dir: Direction) -> Direction:
    match dir:
        case "<":
            return "^"
        case ">":
            return "v"
        case "^":
            return ">"
        case "v":
            return "<"


print(part1(INPUT_FILE_TEST))
print(part1(INPUT_FILE))


def part2(filename: str) -> int:
    rows = file_to_list(filename)
    map_ = [list(x) for x in rows]
    h, w = len(map_), len(map_[0])

    num_loop_options = sum(
        test_if_creates_loop(map_, (i, j)) for (i, j) in product(range(h), range(w))
    )
    return num_loop_options


def test_if_creates_loop(map_: list[list[str]], obstruction: tuple[int, int]) -> bool:
    new_map = copy.deepcopy(map_)
    if new_map[obstruction[0]][obstruction[1]] in "<>^v":
        return False

    new_map[obstruction[0]][obstruction[1]] = "#"
    h, w = len(new_map), len(new_map[0])

    def in_bounds(pos: tuple[int, int]) -> bool:
        return 0 <= pos[0] < h and 0 <= pos[1] < w

    seen = [[set() for _ in range(w)] for __ in range(h)]

    curr_pos, curr_dir = _get_curr_pos_and_dir(new_map)
    while in_bounds(curr_pos):
        if curr_dir in seen[curr_pos[0]][curr_pos[1]]:
            return True
        pos_change = _get_pos_change(curr_dir)
        new_pos = (curr_pos[0] + pos_change[0], curr_pos[1] + pos_change[1])
        if in_bounds(new_pos) and new_map[new_pos[0]][new_pos[1]] == "#":
            curr_dir = _rotate_dir(curr_dir)
        else:
            seen[curr_pos[0]][curr_pos[1]].add(curr_dir)
            curr_pos = new_pos

    return False


print(part2(INPUT_FILE_TEST))
print(part2(INPUT_FILE))
