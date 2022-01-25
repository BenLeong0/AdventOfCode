from itertools import product
from typing import List, Tuple


Coord = Tuple[int, int]
Instruction = Tuple[str, Coord, Coord]


with open("day6.in", "r", newline="") as readfile:
    full_input = [
        (x[0], tuple(map(int, x[1].split(","))), tuple(map(int, x[3].split(","))))
        if x[0] == "toggle" else
        (x[1], tuple(map(int, x[2].split(","))), tuple(map(int, x[4].split(","))))
        for x in [y.split() for y in readfile.readlines()]
    ]


# Part 1

def count_lit_lights(instructions: List[Instruction]) -> int:
    curr_lit = set()
    for instruction in instructions:
        affected_lights = set(product(
            range(instruction[1][0], instruction[2][0] + 1),
            range(instruction[1][1], instruction[2][1] + 1),
        ))
        if instruction[0] == "on":
            curr_lit.update(affected_lights)
        if instruction[0] == "off":
            curr_lit.difference_update(affected_lights)
        if instruction[0] == "toggle":
            curr_lit.symmetric_difference_update(affected_lights)

    return len(curr_lit)

print(count_lit_lights(full_input))


# Part 1

def measure_total_brightness(instructions: List[Instruction]) -> int:
    curr_levels = {(x, y):0 for x,y in product(range(1000), repeat=2)}
    for instruction in instructions:
        for x, y in product(
            range(instruction[1][0], instruction[2][0] + 1),
            range(instruction[1][1], instruction[2][1] + 1),
        ):
            if instruction[0] == "on":
                curr_levels[(x,y)] += 1
            if instruction[0] == "off":
                curr_levels[(x,y)] = max(curr_levels[(x,y)] - 1, 0)
            if instruction[0] == "toggle":
                curr_levels[(x,y)] += 2

    return sum(curr_levels.values())

print(measure_total_brightness(full_input))
