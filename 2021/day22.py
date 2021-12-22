from itertools import product
from typing import List, Tuple

Bounds = Tuple[int, int]

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
def count_activated_cubes(toggles: List[Tuple[int, Tuple[Bounds, Bounds, Bounds]]]) -> int:
    reactor = [[[0] * 101 for _ in range(101)] for __ in range(101)]     # 50 +ve, 50 -ve, 1 zero
    for toggle in toggles:
        for x, y, z in product(
            range(max(-50, toggle[1][0][0]), min(50, toggle[1][0][1]) + 1),
            range(max(-50, toggle[1][1][0]), min(50, toggle[1][1][1]) + 1),
            range(max(-50, toggle[1][2][0]), min(50, toggle[1][2][1]) + 1)
        ):
            reactor[x+50][y+50][z+50] = toggle[0]

    return sum([sum([sum(x) for x in row]) for row in reactor])

assert count_activated_cubes(test_input1) == 590784
assert count_activated_cubes(test_input2) == 474140
print(count_activated_cubes(full_input))


# Part 2
def count_activated_cubes_limitless(toggles: List[Tuple[int, Tuple[Bounds, Bounds, Bounds]]]) -> int:
    on_cubes = set()
    for toggle in toggles:
        for x, y, z in product(
            range(toggle[1][0][0], toggle[1][0][1] + 1),
            range(toggle[1][1][0], toggle[1][1][1] + 1),
            range(toggle[1][2][0], toggle[1][2][1] + 1)
        ):
            on_cubes.add((x,y,z))
            if toggle[0] == 0:
                on_cubes.remove((x,y,z))

    return len(on_cubes)

assert count_activated_cubes_limitless(test_input1) == 590784
assert count_activated_cubes_limitless(test_input2) == 474140
print(count_activated_cubes_limitless(full_input))


a = (1,((0,3),(0,3)))
b = (0,((1,2),(2,4)))
curr_cuboids = []
for switch, bounds in [a,b]:
    new_cuboids = []
    for cuboid in curr_cuboids:
        if not (
            (cuboid[0][0] <= bounds[0][1] and cuboid[0][1] >= bounds[0][0]) and
            (cuboid[1][0] <= bounds[1][1] and cuboid[1][1] >= bounds[1][0])
        ):
            new_cuboids.append(cuboid)
            continue
        # if
    if switch == 1:
        new_cuboids.append(bounds)

