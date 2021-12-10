from collections import defaultdict
from itertools import product
from typing import List, Tuple


test_input: List[Tuple[Tuple[int, int]]] = [
    ((0, 9), (5, 9)),
    ((8, 0), (0, 8)),
    ((9, 4), (3, 4)),
    ((2, 2), (2, 1)),
    ((7, 0), (7, 4)),
    ((6, 4), (2, 0)),
    ((0, 9), (2, 9)),
    ((3, 4), (1, 4)),
    ((0, 0), (8, 8)),
    ((5, 5), (8, 2)),
]

with open("day5.in", "r", newline="\n") as readfile:
    full_input = [
        tuple(tuple(map(int,y.split(","))) for y in x[:-1].split(" -> "))
        for x in readfile.readlines()
    ]


# Shared
def find_number_of_dangerous_spots(
    coord_pairs: List[Tuple[Tuple[int, int]]],
    include_diagonals: bool = False,
) -> int:
    spot_count = defaultdict(int)

    for coord_pair in coord_pairs:
        x1, y1, x2, y2 = coord_pair[0] + coord_pair[1]
        curr_spots = []
        if x1 == x2 or y1 == y2:
            curr_spots += list(product(
                range(min(x1, x2), max(x1,x2)+1),
                range(min(y1, y2), max(y1,y2)+1)
            ))
        elif include_diagonals and (y2-y1)/(x2-x1) in (1,-1):
            curr_spots += list(zip(
                range(min(x1, x2), max(x1, x2)+1),
                range(min(y1, y2), max(y1, y2)+1)[::(y2-y1)//(x2-x1)]
            ))

        for spot in curr_spots:
            spot_count[spot] += 1

    return len([x for x in spot_count if spot_count[x] > 1])

# Part 1
assert find_number_of_dangerous_spots(test_input) == 5
print(find_number_of_dangerous_spots(full_input))

# Part 2
assert find_number_of_dangerous_spots(test_input, True) == 12
print(find_number_of_dangerous_spots(full_input, True))

