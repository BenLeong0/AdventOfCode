from typing import List, Tuple


test_input = [
    ("forward", 5),
    ("down", 5),
    ("forward", 8),
    ("up", 3),
    ("down", 8),
    ("forward", 2),
]

with open("day2.in", "r") as readfile:
    raw_input = [x.split() for x in readfile.readlines()]
    full_input = [(x[0], int(x[1])) for x in raw_input]


# Part 1
def total_displacement(movements: List[Tuple[str, int]]) -> int:
    forwards_displacement = 0
    vertical_displacement = 0

    for (direction, distance) in movements:
        if direction == "forward":
            forwards_displacement += distance
        elif direction == "down":
            vertical_displacement += distance
        elif direction == "up":
            vertical_displacement -= distance

    return forwards_displacement * vertical_displacement

assert total_displacement(test_input) == 150
print(total_displacement(full_input))


# Part 2
def total_displacement_with_aim(movements: List[Tuple[str, int]]) -> int:
    forwards_displacement = 0
    vertical_displacement = 0
    aim = 0

    for (direction, change) in movements:
        if direction == "forward":
            forwards_displacement += change
            vertical_displacement += change * aim
        elif direction == "down":
            aim += change
        elif direction == "up":
            aim -= change

    return forwards_displacement * vertical_displacement

assert total_displacement_with_aim(test_input) == 900
print(total_displacement_with_aim(full_input))
