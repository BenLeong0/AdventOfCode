import copy
from itertools import product
import time
from typing import List, Literal, Optional, Set, Tuple


Coord = Tuple[int,int,int]
BeaconList = List[Coord]
BeaconSet = Set[Coord]


def get_input(filename: str) -> List[BeaconList]:
    with open(filename, "r", newline="\n") as readfile:
        file = readfile.read().replace('\r\n', '\n').split('\n\n')
        return [
            [
                tuple(int(x) for x in row.split(','))
                for row in coords.split('\n')[1:]
            ] for coords in file[:-1]
        ]

test_input = get_input("day19_test.in")
full_input = get_input("day19.in")


# Shared

def rotate_around_axis(coord: Coord, axis: Literal[0,1,2]) -> Coord:
    return [
        lambda x,y,z: (x,z,-y),
        lambda x,y,z: (z,y,-x),
        lambda x,y,z: (y,-x,z),
    ][axis](*coord)

def get_all_orientations(beacon_list: List[Coord]) -> List[List[Coord]]:
    beacon_list = copy.deepcopy(beacon_list)
    orientations = []
    for dir in range(4):
        for _ in range(4):
            orientations.append(copy.deepcopy(beacon_list))
            beacon_list = [rotate_around_axis(coord, dir%2) for coord in beacon_list]
        beacon_list = [rotate_around_axis(coord, 2) for coord in beacon_list]

    beacon_list = [rotate_around_axis(coord, 1) for coord in beacon_list]
    for __ in range(4):
        orientations.append(copy.deepcopy(beacon_list))
        beacon_list = [rotate_around_axis(coord, 2) for coord in beacon_list]

    beacon_list = [rotate_around_axis(rotate_around_axis(coord, 1), 1) for coord in beacon_list]
    for __ in range(4):
        orientations.append(copy.deepcopy(beacon_list))
        beacon_list = [rotate_around_axis(coord, 2) for coord in beacon_list]

    return orientations

assert len({b_list[4] for b_list in get_all_orientations([
    (-1,-1,1),
    (-2,-2,2),
    (-3,-3,3),
    (-2,-3,1),
    (5,6,-4),
    (8,0,7),
])}) == 24


# Part 1
def get_transformed_beacon_set(
    transformed_beacon_set: BeaconSet,
    beacon_list: BeaconList
) -> Tuple[bool, Optional[Set[Coord]], Optional[Coord]]:
    for coord1 in transformed_beacon_set:
        for oriented_beacon_list in get_all_orientations(beacon_list):
            for coord2 in oriented_beacon_list:
                # print(coord1, coord2)
                transformation = tuple(x-y for x,y in zip(coord1, coord2))
                new_beacon_set = {tuple(x+y for x,y in zip(coord, transformation)) for coord in oriented_beacon_list}
                if len(transformed_beacon_set.intersection(new_beacon_set)) >= 12:
                    return True, new_beacon_set, transformation
    return False, None, None


def get_number_of_beacons(beacon_lists: List[BeaconList]) -> int:
    beacon_lists = copy.deepcopy(beacon_lists)
    transformed_beacon_sets = [set(beacon_lists.pop(0))]
    while beacon_lists:
        print(len(beacon_lists), len(transformed_beacon_sets))
        for transformed_beacon_set, i in product(
            transformed_beacon_sets, range(len(beacon_lists))
        ):
            transformed, new_set, _ = get_transformed_beacon_set(transformed_beacon_set, beacon_lists[i])
            if transformed:
                transformed_beacon_sets.append(new_set)
                beacon_lists.pop(i)
                break

    return len(set().union(*transformed_beacon_sets))

assert get_number_of_beacons(test_input) == 79
print(get_number_of_beacons(full_input))    # Takes > 10 minutes


# Part 2
def get_largest_manhatten_distance(beacon_lists: List[BeaconList]) -> int:
    beacon_lists = copy.deepcopy(beacon_lists)
    transformed_beacon_sets = [set(beacon_lists.pop(0))]
    scanner_locations = [(0,0,0)]
    while beacon_lists:
        print(len(beacon_lists), len(transformed_beacon_sets))
        for i, transformed_beacon_set in product(
            range(len(beacon_lists)), transformed_beacon_sets
        ):
            transformed, new_set, scanner_location = get_transformed_beacon_set(transformed_beacon_set, beacon_lists[i])
            if transformed:
                transformed_beacon_sets.append(new_set)
                scanner_locations.append(scanner_location)
                beacon_lists.pop(i)
                break

    max_distance = 0
    for coord1 in scanner_locations:
        for coord2 in scanner_locations:
            max_distance = max(max_distance, sum([abs(x-y) for x,y in zip(coord1, coord2)]))

    return max_distance

assert get_largest_manhatten_distance(test_input) == 3621
print(get_largest_manhatten_distance(full_input))   # 344.9102027 seconds
