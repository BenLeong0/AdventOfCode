import copy
from typing import List, Literal, Set, Tuple


test_dots: Set[Tuple[int, int]] = {
    (6, 10),
    (0, 14),
    (9, 10),
    (0, 3),
    (10, 4),
    (4, 11),
    (6, 0),
    (6, 12),
    (4, 1),
    (0, 13),
    (10, 12),
    (3, 4),
    (3, 0),
    (8, 4),
    (1, 10),
    (2, 14),
    (8, 10),
    (9, 0),
}

test_folds: List[Tuple[Literal["x","y"], int]] = [
    ("y", 7),
    ("x", 5),
]

with open("inputs/day13.in", "r", newline="\n") as readfile:
    file = readfile.read().replace('\r\n', '\n').split('\n\n')
    full_dots = {eval("("+x+")") for x in file[0].split('\n')}
    full_folds = [(x.split("=")[0][-1], int(x.split("=")[1])) for x in file[1].split("\n")[:-1]]


# Part 1
def count_visible_dots_after_folding_once(
    dots: Set[Tuple[int, int]],
    folds: List[Tuple[Literal["x","y"], int]]
) -> int:
    dots = copy.deepcopy(dots)
    axis, coord = folds[0]
    idx = 0 if axis == "x" else 1
    for dot in tuple(filter(lambda d: d[idx] > coord, dots)):
        new_dot = list(dot)
        new_dot[idx] = 2*coord - new_dot[idx]
        dots.add(tuple(new_dot))
        dots.remove(dot)

    return len(dots)

assert count_visible_dots_after_folding_once(test_dots, test_folds) == 17
print(count_visible_dots_after_folding_once(full_dots, full_folds))


# Part 2
def get_code(
    dots: Set[Tuple[int, int]],
    folds: List[Tuple[Literal["x","y"], int]]
) -> List[List[Literal["#","."]]]:
    dots = copy.deepcopy(dots)
    for (axis, coord) in folds:
        idx = 0 if axis == "x" else 1
        for dot in tuple(filter(lambda d: d[idx] > coord, dots)):
            new_dot = list(dot)
            new_dot[idx] = 2*coord - new_dot[idx]
            dots.add(tuple(new_dot))
            dots.remove(dot)

        if axis == "x":
            width = coord
        else:
            height = coord

    matrix = [[" "] * width for _ in range(height)]
    for (x,y) in dots:
        matrix[y][x] = "█"
    return '\n'.join([''.join(row) for row in matrix])

print(get_code(full_dots, full_folds))

# ████ ████   ██ █  █ ████ █    ███  █
# █    █       █ █ █     █ █    █  █ █
# ███  ███     █ ██     █  █    ███  █
# █    █       █ █ █   █   █    █  █ █
# █    █    █  █ █ █  █    █    █  █ █
# ████ █     ██  █  █ ████ ████ ███  ████
