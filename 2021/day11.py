import copy
from typing import List, Optional, Set, Tuple


test_input: List[List[int]] = [
    [5,4,8,3,1,4,3,2,2,3],
    [2,7,4,5,8,5,4,7,1,1],
    [5,2,6,4,5,5,6,1,7,3],
    [6,1,4,1,3,3,6,1,4,6],
    [6,3,5,7,3,8,5,4,7,8],
    [4,1,6,7,5,2,4,6,4,5],
    [2,1,7,6,8,4,1,7,2,1],
    [6,8,8,2,8,8,1,1,3,4],
    [4,8,4,6,8,4,8,5,5,4],
    [5,2,8,3,7,5,1,5,2,6],
]


full_input: List[List[int]] = [
    [2,2,3,8,5,1,8,6,1,4],
    [4,5,5,2,3,8,8,5,5,3],
    [2,5,6,2,1,2,1,1,4,3],
    [2,6,6,6,6,8,5,3,3,7],
    [7,5,7,5,5,1,8,7,8,4],
    [3,5,7,2,5,3,4,8,7,1],
    [8,4,1,1,7,1,8,2,8,3],
    [7,7,4,2,6,6,8,3,8,5],
    [1,2,3,5,1,3,3,2,3,1],
    [2,5,4,6,1,6,5,3,4,5],
]


# Shared
def increment_grid(octopuses: List[List[int]]) -> None:
    for i in range(len(octopuses)):
        for j in range(len(octopuses[0])):
            octopuses[i][j] += 1


def reset_flashers(octopuses: List[List[int]]) -> None:
    for i in range(len(octopuses)):
        for j in range(len(octopuses[0])):
            if octopuses[i][j] > 9:
                octopuses[i][j] = 0


def get_flashers(octopuses: List[List[int]], flashed: Set[Tuple[int,int]]) -> None:
    flashers = []
    for i in range(len(octopuses)):
        for j in range(len(octopuses[0])):
            if (i,j) not in flashed and octopuses[i][j] > 9:
                flashers.append((i,j))
    return flashers


def get_neighbourhood(octopuses: List[List[int]], i: int, j: int) -> List[Tuple[int, int]]:
    height = len(octopuses)
    width = len(octopuses[0])
    return [ 
        (x,y) 
        for x in range(i-1,i+2) if 0 <= x < height
        for y in range(j-1,j+2) if 0 <= y < width
    ]


# Part 1
def count_flashes(octopuses: List[List[int]], steps: int = 100) -> int:
    octopuses = copy.deepcopy(octopuses)
    total = 0

    for _ in range(steps):
        flashed: Set[Tuple[int,int]] = set()
        increment_grid(octopuses)
        while len(flashers := get_flashers(octopuses, flashed)) > 0:
            for (i,j) in flashers:
                flashed.add((i,j))
                for (nb_i, nb_j) in get_neighbourhood(octopuses, i, j):
                    octopuses[nb_i][nb_j] += 1
                total += 1
        reset_flashers(octopuses)
    
    return total

assert count_flashes(test_input, steps=10) == 204
assert count_flashes(test_input) == 1656
print(count_flashes(full_input))


# Part 2
def find_first_synchronised_flash(octopuses: List[List[int]]) -> int:
    octopuses = copy.deepcopy(octopuses)
    step = 1

    while True:
        flashed: Set[Tuple[int,int]] = set()
        increment_grid(octopuses)
        while len(flashers := get_flashers(octopuses, flashed)) > 0:
            for (i,j) in flashers:
                flashed.add((i,j))
                for (nb_i, nb_j) in get_neighbourhood(octopuses, i, j):
                    octopuses[nb_i][nb_j] += 1
        reset_flashers(octopuses)

        if len(flashed) == 100:
            return step
        step += 1
    
assert find_first_synchronised_flash(test_input) == 195
print(find_first_synchronised_flash(full_input))
