from copy import deepcopy
from itertools import product
from typing import List, Literal, Tuple


Light = Literal["#", "."]


test_input: List[List[Light]] = [
    [char for char in ".#.#.#"],
    [char for char in "...##."],
    [char for char in "#....#"],
    [char for char in "..#..."],
    [char for char in "#.#..#"],
    [char for char in "####.."],
]

with open('inputs/day18.in', "r", newline="") as readfile:
    full_input: List[List[Light]] = [[char for char in row[:-1]] for row in readfile.readlines()]

# Shared

def num_lit_neighbours(grid: List[List[Light]], pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    return sum([
        grid[pos[0] + x][pos[1] + y] == "#" for x, y in product((-1,0,1), repeat=2)
        if abs(x)+abs(y)!=0 and 0<=pos[0]+x<len(grid) and 0<=pos[1]+y<len(grid[0])
    ])


# Part 1

def get_number_of_lit_lights(initial_grid: List[List[Light]], steps: int) -> int:
    curr_grid = deepcopy(initial_grid)
    for _ in range(steps):
        curr_grid = [
            [
                ("#" if num_lit_neighbours(curr_grid, (i,j)) in (2,3) else '.')
                if curr_grid[i][j] == "#" else
                ("#" if num_lit_neighbours(curr_grid, (i,j)) == 3 else '.')
                for j in range(len(curr_grid[i]))
            ]
            for i in range(len(curr_grid))
        ]
    return sum([sum([x == "#" for x in row]) for row in curr_grid])

assert get_number_of_lit_lights(test_input, 4) == 4
print(get_number_of_lit_lights(full_input, 100))


# Part 2

def get_number_of_lit_lights_broken(initial_grid: List[List[Light]], steps: int) -> int:
    curr_grid = deepcopy(initial_grid)
    for (i, j) in product((-1, 0), repeat=2):
        curr_grid[i][j] = "#"
    for _ in range(steps):
        curr_grid = [
            [
                (
                    ("#" if num_lit_neighbours(curr_grid, (i,j)) in (2,3) else '.')
                    if curr_grid[i][j] == "#" else
                    ("#" if num_lit_neighbours(curr_grid, (i,j)) == 3 else '.')
                ) if (i, j) not in product((len(curr_grid)-1, 0), repeat=2) else "#"
                for j in range(len(curr_grid[i]))
            ]
            for i in range(len(curr_grid))
        ]
    return sum([sum([x == "#" for x in row]) for row in curr_grid])

assert get_number_of_lit_lights_broken(test_input, 5) == 17
print(get_number_of_lit_lights_broken(full_input, 100))
