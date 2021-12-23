from itertools import product
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

test_input1 = get_input("day22_test1.in")
test_input2 = get_input("day22_test2.in")
full_input = get_input("day22.in")


# Part 1
def count_activated_cubes(toggles: List[Tuple[int, Cuboid]]) -> int:
    reactor = [[[0] * 101 for _ in range(101)] for _ in range(101)]     # 50 +ve, 50 -ve, 1 zero
    for state, cuboid in toggles:
        for x, y, z in product(
            range(max(-50, cuboid[X][MIN]), min(50, cuboid[X][MAX]) + 1),
            range(max(-50, cuboid[Y][MIN]), min(50, cuboid[Y][MAX]) + 1),
            range(max(-50, cuboid[Z][MIN]), min(50, cuboid[Z][MAX]) + 1)
        ):
            reactor[x+50][y+50][z+50] = state

    return sum([sum([sum(x) for x in plane]) for plane in reactor])

assert count_activated_cubes(test_input1) == 590784
assert count_activated_cubes(test_input2) == 474140
print(count_activated_cubes(full_input))


# Part 2

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

def count_activated_cubes_limitless(toggles: List[Tuple[int, Cuboid]]) -> int:
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

assert count_activated_cubes_limitless(test_input2) == 2758514936282235
print(count_activated_cubes_limitless(full_input))
