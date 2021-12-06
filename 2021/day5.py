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


# Part 1
def find_number_of_dangerous_spots(coord_pairs: List[Tuple[Tuple[int, int]]]) -> int:
    spots_seen_once = set()
    spots_seen_more_than_once = set()

    for coord_pair in coord_pairs:
        if coord_pair[0][0] == coord_pair[1][0]:
            inc_dir = 1 if coord_pair[0][1] < coord_pair[1][1] else -1
            curr_spots = [
                (coord_pair[0][0], coord_pair[0][1] + inc_dir * step)
                for step in range(abs(coord_pair[0][1] - coord_pair[1][1]) + 1)
            ]
        elif coord_pair[0][1] == coord_pair[1][1]:
            inc_dir = 1 if coord_pair[0][0] < coord_pair[1][0] else -1
            curr_spots = [
                (coord_pair[0][0] + inc_dir * step, coord_pair[0][1])
                for step in range(abs(coord_pair[0][0] - coord_pair[1][0]) + 1)
            ]
        else:
            continue

        for spot in curr_spots:
            if spot in spots_seen_once:
                spots_seen_more_than_once.add(spot)
            else:
                spots_seen_once.add(spot)

    return len(spots_seen_more_than_once)

assert find_number_of_dangerous_spots(test_input) == 5
print(find_number_of_dangerous_spots(full_input))


# Part 2
def find_number_of_dangerous_spots_with_diag(coord_pairs: List[Tuple[Tuple[int, int]]]) -> int:
    spots_seen_once = set()
    spots_seen_more_than_once = set()

    for coord_pair in coord_pairs:
        if coord_pair[0][0] == coord_pair[1][0]:
            inc_dir = 1 if coord_pair[0][1] < coord_pair[1][1] else -1
            curr_spots = [
                (coord_pair[0][0], coord_pair[0][1] + inc_dir * step)
                for step in range(abs(coord_pair[0][1] - coord_pair[1][1]) + 1)
            ]
        elif coord_pair[0][1] == coord_pair[1][1]:
            inc_dir = 1 if coord_pair[0][0] < coord_pair[1][0] else -1
            curr_spots = [
                (coord_pair[0][0] + inc_dir * step, coord_pair[0][1])
                for step in range(abs(coord_pair[0][0] - coord_pair[1][0]) + 1)
            ]
        elif abs(coord_pair[0][0] - coord_pair[1][0]) == abs(coord_pair[0][1] - coord_pair[1][1]):
            x_inc_dir = 1 if coord_pair[0][0] < coord_pair[1][0] else -1
            y_inc_dir = 1 if coord_pair[0][1] < coord_pair[1][1] else -1
            curr_spots = [
                (coord_pair[0][0] + x_inc_dir * step, coord_pair[0][1] + y_inc_dir * step)
                for step in range(abs(coord_pair[0][0] - coord_pair[1][0]) + 1)
            ]
        else:
            continue

        for spot in curr_spots:
            if spot in spots_seen_once:
                spots_seen_more_than_once.add(spot)
            else:
                spots_seen_once.add(spot)

    return len(spots_seen_more_than_once)

assert find_number_of_dangerous_spots_with_diag(test_input) == 12
print(find_number_of_dangerous_spots_with_diag(full_input))

