import copy
from itertools import product
from typing import List, Literal


Coord = Literal[".",">","v",">x","vx"]
Layout = List[List[Coord]]

test_input: Layout = [
    ["v",".",".",".",">",">",".","v","v",">"],
    [".","v","v",">",">",".","v","v",".","."],
    [">",">",".",">","v",">",".",".",".","v"],
    [">",">","v",">",">",".",">",".","v","."],
    ["v",">","v",".","v","v",".","v",".","."],
    [">",".",">",">",".",".","v",".",".","."],
    [".","v","v",".",".",">",".",">","v","."],
    ["v",".","v",".",".",">",">","v",".","v"],
    [".",".",".",".","v",".",".","v",".",">"],
]

with open("day25.in", "r", newline="\n") as readfile:
    full_input: Layout = [list(line.replace("\n","")) for line in readfile.readlines()]

def print_layout(layout: Layout):
    for row in layout:
        print(''.join(row))
    print('='*len(layout[0]))


# Part 1
def find_min_stationary_steps(layout: Layout) -> int:
    prev_layout = None
    height, width = len(layout), len(layout[0])
    steps = 0
    while layout != prev_layout:
        prev_layout, layout = layout, copy.deepcopy(layout)
        for i, j in product(range(height), range(width)):
            if layout[i][j] == ">" and layout[i][(j+1)%width] == ".":
                layout[i][j], layout[i][(j+1)%width] = ".x", ">x"
        for i, j in product(range(height), range(width)):
            if layout[i][j] == ".x":
                layout[i][j] = "."
        for i, j in product(range(height), range(width)):
            if layout[i][j] == "v" and layout[(i+1)%height][j] == ".":
                layout[i][j], layout[(i+1)%height][j] = ".x", "vx"
        for i, j in product(range(height), range(width)):
            if layout[i][j] == ">x":
                layout[i][j] = ">"
            elif layout[i][j] == "vx":
                layout[i][j] = "v"
            elif layout[i][j] == ".x":
                layout[i][j] = "."
        steps += 1
    return steps

assert find_min_stationary_steps(test_input) == 58
print(find_min_stationary_steps(full_input))
