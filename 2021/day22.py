import copy
from typing import List, Literal, Optional, Tuple

Bounds = Tuple[int, int]
Cuboid = Tuple[Bounds, Bounds, Bounds]
X, Y, Z = 0, 1, 2
MIN, MAX = 0, 1

def get_input(filename: str) -> List[Tuple[int, Tuple[Bounds, Bounds, Bounds]]]:
    with open(filename, "r", newline="\n") as readfile:
        file = readfile.read().replace('\r\n', '\n').split('\n')
        return [
            (
                1 if row.split()[0] == "on" else 0,
                tuple(
                    (int(x[2:].split("..")[0]), int(x[2:].split("..")[1]))
                    for x in row.split()[1].split(',')
                )
            ) for row in file
        ]

test_input1 = get_input("input_files/day22_test1.in")
test_input2 = get_input("input_files/day22_test2.in")
full_input = get_input("input_files/day22.in")


# Shared
def check_if_intersect(cuboid1: Cuboid, cuboid2: Cuboid) -> bool:
    return (
        max(cuboid1[X][MIN], cuboid2[X][MIN]) <= min(cuboid1[X][MAX], cuboid2[X][MAX]) and
        max(cuboid1[Y][MIN], cuboid2[Y][MIN]) <= min(cuboid1[Y][MAX], cuboid2[Y][MAX]) and
        max(cuboid1[Z][MIN], cuboid2[Z][MIN]) <= min(cuboid1[Z][MAX], cuboid2[Z][MAX])
    )


def get_intersection(cuboid1: Cuboid, cuboid2: Cuboid) -> Optional[Cuboid]:
    return (
        (max(cuboid1[X][MIN], cuboid2[X][MIN]), min(cuboid1[X][MAX], cuboid2[X][MAX])),
        (max(cuboid1[Y][MIN], cuboid2[Y][MIN]), min(cuboid1[Y][MAX], cuboid2[Y][MAX])),
        (max(cuboid1[Z][MIN], cuboid2[Z][MIN]), min(cuboid1[Z][MAX], cuboid2[Z][MAX])),
    )

def get_volume(cuboid: Cuboid) -> int:
    return (
        (cuboid[X][MAX] - cuboid[X][MIN] + 1) *
        (cuboid[Y][MAX] - cuboid[Y][MIN] + 1) *
        (cuboid[Z][MAX] - cuboid[Z][MIN] + 1)
    )

def count_activated_cubes(toggles: List[Tuple[int, Cuboid]]) -> int:
    seen_cuboids: List[Tuple[Literal[-1, 1], Cuboid]] = []
    for state, cuboid in toggles:
        new_cuboids = []
        for sign, seen_cuboid in seen_cuboids:
            if check_if_intersect(cuboid, seen_cuboid):
                new_cuboids.append((-sign, get_intersection(cuboid, seen_cuboid)))
        seen_cuboids += new_cuboids
        if state == 1:
            seen_cuboids.append((1, cuboid))
    return sum([sign * get_volume(cuboid) for sign, cuboid in seen_cuboids])


# Part 1
RESTRICTION = ((-50, 50), (-50, 50), (-50, 50))

def count_activated_cubes_restricted(toggles: List[Tuple[int, Cuboid]]) -> int:
    restricted_toggles = [
        (state, get_intersection(cuboid, RESTRICTION)) for state, cuboid in
        filter(
            lambda x: check_if_intersect(x[1], RESTRICTION),
            copy.deepcopy(toggles)
        )
    ]
    return count_activated_cubes(restricted_toggles)

assert count_activated_cubes_restricted(test_input1) == 590784
assert count_activated_cubes_restricted(test_input2) == 474140
print(count_activated_cubes_restricted(full_input))


# Part 2
assert count_activated_cubes(test_input2) == 2758514936282235
print(count_activated_cubes(full_input))
