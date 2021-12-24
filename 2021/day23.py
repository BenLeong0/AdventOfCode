import copy
from functools import partial
from typing import Dict, List, Literal, Optional, Set, Tuple, TypedDict

test_input = [
    list("#############"),
    list("#...........#"),
    list("###B#C#B#D###"),
    list("  #A#D#C#A#  "),
    list("  #########  "),
]

full_input = [
    list("#############"),
    list("#...........#"),
    list("###B#A#A#D###"),
    list("  #D#C#B#C#  "),
    list("  #########  "),
]

## Reduce to:
# □□-□-□-□-□□
#   □ □ □ □
#   □ □ □ □

ROOM_COORDS = { "A": 3, "B": 5, "C": 7, "D": 9 }
STEP_COSTS = { "A": 1, "B": 10, "C": 100, "D": 1000 }

Map = List[List[str]]
Coord = Tuple[int, int]

# Part 1
Coord = Literal["H0","H1","H2","H3","H4","H5","H6","A0","B0","C0","D0","A1","B1","C1","D1"]
BugType = Literal["A","B","C","D"]
class CoordInfo(TypedDict):
    curr: Optional[BugType]
    adj: Set[Tuple[Coord, int]]
Map = Dict[Coord, CoordInfo]


def is_at_home(coord: Coord, map: Map, bug_type: BugType) -> bool:
    return (
        (coord == bug_type + '1') or
        (coord == bug_type + '0' and map[bug_type + '1']["curr"] == bug_type)
    )

def is_not_trapped(coord: Coord, map: Map) -> bool:
    return coord[1] != "1" or map[coord[0] + '0']["curr"] is None

def is_active(coord: Coord, map: Map) -> bool:
    return not is_at_home(coord, map, map[coord]["curr"]) and is_not_trapped(coord, map)

def get_print_layout(map: Map) -> str:
    f = lambda coord: map[coord]["curr"] if map[coord]["curr"] is not None else '.'
    return (
        f("H0") + f("H1") + " " + f("H2") + " " + f("H3") +
        " " + f("H4") + " " + f("H5") + f("H6") + "\n  " +
        f("A0") + " " + f("B0") + " " + f("C0") + " " + f("D0") + "\n  " +
        f("A1") + " " + f("B1") + " " + f("C1") + " " + f("D1") + "\n==========="
    )

def make_move(map: Map, memo: Dict[str, int]) -> int:
    if (layout := get_current_layout(map)) in memo:
        return memo[layout]

    bug_locations = [coord for coord in map if map[coord]["curr"] is not None]
    active_bug_locations = list(filter(partial(is_active, map=map), bug_locations))

    routes: List[Tuple[Coord, Coord, int]] = []
    for coord in active_bug_locations:
        energy_costs = {coord: 0}
        bug_type: BugType = map[coord]["curr"]
        curr_coord = coord

        if curr_coord[0] != "H" and curr_coord[1] == "1":       # Already filtered out if trapped
            curr_coord = curr_coord[0] + '0'                    # Move from deep to shallow
            energy_costs[curr_coord] = STEP_COSTS[bug_type]

        stack = [curr_coord]
        while stack:
            curr_coord = stack.pop()
            if is_at_home(curr_coord, map, bug_type):
                new_map = copy.deepcopy(map)
                new_map[curr_coord]["curr"], new_map[coord]["curr"] = new_map[coord]["curr"], None
                memo[layout] = (total_energy_cost := energy_costs[curr_coord] + make_move(new_map, memo))
                return total_energy_cost
            adj_points = [
                (x, y) for x, y in map[curr_coord]["adj"]
                if x not in energy_costs and map[x]["curr"] is None and x[0][0] in {"H", bug_type}
            ]
            for new_coord, dist in adj_points:
                energy_costs[new_coord] = energy_costs[curr_coord] + dist * STEP_COSTS[bug_type]
                stack.append(new_coord)
        routes += [
            (coord, end_coord, energy_cost) for end_coord, energy_cost in energy_costs.items()
            if end_coord[0] == "H" and coord[0] != "H"
        ]

    min_energy = float("inf")
    for start_coord, end_coord, move_energy_cost in routes:
        new_map = copy.deepcopy(map)
        new_map[end_coord]["curr"], new_map[start_coord]["curr"] = new_map[start_coord]["curr"], None
        total_energy_cost = move_energy_cost + make_move(new_map, memo)
        min_energy = min(min_energy, total_energy_cost)
    memo[layout] = min_energy
    return min_energy

def get_current_layout(map: Map) -> str:
    return '_'.join([k + str(v["curr"]) for k,v in sorted(map.items())])

def get_min_energy(inpt: List[List[str]]) -> int:
    start_map: Map = {
        "H0": {"curr": None,        "adj": {("H1", 1)}},
        "H1": {"curr": None,        "adj": {("H0", 1), ("H2", 2), ("A0", 2)}},
        "H2": {"curr": None,        "adj": {("H1", 2), ("H3", 2), ("A0", 2), ("B0", 2)}},
        "H3": {"curr": None,        "adj": {("H2", 2), ("H4", 2), ("B0", 2), ("C0", 2)}},
        "H4": {"curr": None,        "adj": {("H3", 2), ("H5", 2), ("C0", 2), ("D0", 2)}},
        "H5": {"curr": None,        "adj": {("H4", 2), ("H6", 1), ("D0", 2)}},
        "H6": {"curr": None,        "adj": {("H5", 1)}},
        "A0": {"curr": inpt[2][3],  "adj": {("H1", 2), ("H2", 2), ("A1", 1)}},
        "B0": {"curr": inpt[2][5],  "adj": {("H2", 2), ("H3", 2), ("B1", 1)}},
        "C0": {"curr": inpt[2][7],  "adj": {("H3", 2), ("H4", 2), ("C1", 1)}},
        "D0": {"curr": inpt[2][9],  "adj": {("H4", 2), ("H5", 2), ("D1", 1)}},
        "A1": {"curr": inpt[3][3],  "adj": {("A0", 1)}},
        "B1": {"curr": inpt[3][5],  "adj": {("B0", 1)}},
        "C1": {"curr": inpt[3][7],  "adj": {("C0", 1)}},
        "D1": {"curr": inpt[3][9],  "adj": {("D0", 1)}},
    }
    finished_layout = 'A0A_A1A_B0B_B1B_C0C_C1C_D0D_D1D_H0None_H1None_H2None_H3None_H4None_H5None_H6None'
    memo: Dict[str, int] = {finished_layout: 0}
    return make_move(start_map, memo=memo)

# get_min_energy(test_input) == 12521
print(get_min_energy(full_input)) # 15241 is wrong!
