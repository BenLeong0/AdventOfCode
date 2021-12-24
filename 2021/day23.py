import copy
from functools import partial
from typing import Dict, List, Literal, Optional, Set, Tuple, TypedDict

test_input = [
    "#############",
    "#...........#",
    "###B#C#B#D###",
    "  #A#D#C#A#  ",
    "  #########  ",
]

full_input = [
    "#############",
    "#...........#",
    "###B#A#A#D###",
    "  #D#C#B#C#  ",
    "  #########  ",
]


# Shared
STEP_COSTS = { "A": 1, "B": 10, "C": 100, "D": 1000 }

Coord = Literal["H0","H1","H2","H3","H4","H5","H6","A0","B0","C0","D0","A1","B1","C1","D1"]
BugType = Literal["A","B","C","D"]
class CoordInfo(TypedDict):
    curr: Optional[BugType]
    adj: Set[Tuple[Coord, int]]
Map = Dict[Coord, CoordInfo]

def is_at_home(coord: Coord, map: Map, bug_type: BugType) -> bool:
    if coord[0] != bug_type:
        return False
    return all(
        map[coord2]["curr"] == bug_type for coord2 in map
        if coord2[0] == bug_type and int(coord2[1]) > int(coord[1])
    )


# Part 1
def is_not_trapped(coord: Coord, map: Map) -> bool:
    return coord[1] != "1" or coord[0] == "H" or map[coord[0] + '0']["curr"] is None

def is_moveable(coord: Coord, map: Map) -> bool:
    return not is_at_home(coord, map, map[coord]["curr"]) and is_not_trapped(coord, map)

def get_print_layout(map: Map) -> str:
    f = lambda coord: map[coord]["curr"] if map[coord]["curr"] is not None else '.'
    return (
        f("H0") + f("H1") + " " + f("H2") + " " + f("H3") +
        " " + f("H4") + " " + f("H5") + f("H6") + "\n  " +
        f("A0") + " " + f("B0") + " " + f("C0") + " " + f("D0") + "\n  " +
        f("A1") + " " + f("B1") + " " + f("C1") + " " + f("D1") + "\n==========="
    )

def get_min_energy(map: Map, min_energy_memo: Dict[str, int]) -> int:
    if (layout := get_current_layout(map)) in min_energy_memo:
        return min_energy_memo[layout]

    min_energy_memo[layout] = float("inf")
    bug_locations: List[Coord] = [coord for coord, data in map.items() if data["curr"] is not None]
    moveable_bug_locations = list(filter(partial(is_moveable, map=map), bug_locations))

    for coord in moveable_bug_locations:
        energy_costs: Dict[Coord, int] = {coord: 0}
        bug_type: BugType = map[coord]["curr"]
        curr_coord = coord

        if curr_coord[0] != "H" and curr_coord[1] == "1":       # Already filtered out if trapped
            curr_coord: Coord = curr_coord[0] + '0'                    # Move from deep to shallow
            energy_costs[curr_coord] = STEP_COSTS[bug_type]

        stack: List[Coord] = [curr_coord]       # Iterative DFS
        while stack:
            curr_coord = stack.pop()
            if is_at_home(curr_coord, map, bug_type):
                new_map = copy.deepcopy(map)
                new_map[curr_coord]["curr"], new_map[coord]["curr"] = new_map[coord]["curr"], None
                min_energy_memo[layout] = energy_costs[curr_coord] + get_min_energy(new_map, min_energy_memo)
                return min_energy_memo[layout]
            for adj_coord, dist in map[curr_coord]["adj"]:
                if (
                    adj_coord in energy_costs or
                    map[adj_coord]["curr"] is not None or
                    adj_coord[0] not in {"H", bug_type}
                ):
                    continue
                energy_costs[adj_coord] = energy_costs[curr_coord] + dist * STEP_COSTS[bug_type]
                stack.append(adj_coord)

        for end_coord, move_energy_cost in energy_costs.items():
            if end_coord[0] != "H" or coord[0] == "H":
                continue
            new_map = copy.deepcopy(map)
            new_map[end_coord]["curr"], new_map[coord]["curr"] = new_map[coord]["curr"], None
            total_energy_cost = move_energy_cost + get_min_energy(new_map, min_energy_memo)
            min_energy_memo[layout] = min(min_energy_memo[layout], total_energy_cost)

    return min_energy_memo[layout]

def get_current_layout(map: Map) -> str:
    return '_'.join([k + str(v["curr"]) for k,v in sorted(map.items())])

def get_min_energy_init(inpt: List[str]) -> int:
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
    return get_min_energy(start_map, min_energy_memo=memo)

assert get_min_energy_init(test_input) == 12521
print(get_min_energy_init(full_input))


# Part 2
STEP_COSTS = { "A": 1, "B": 10, "C": 100, "D": 1000 }

Coord = Literal[
    "H0","H1","H2","H3","H4","H5","H6",
    "A0","B0","C0","D0","A1","B1","C1","D1",
    "A2","B2","C2","D2","A3","B3","C3","D3"
]
BugType = Literal["A","B","C","D"]
class CoordInfo(TypedDict):
    curr: Optional[BugType]
    adj: Set[Tuple[Coord, int]]
Map = Dict[Coord, CoordInfo]

def get_print_layout(map: Map) -> str:
    f = lambda coord: map[coord]["curr"] if map[coord]["curr"] is not None else '.'
    return (
        f("H0") + f("H1") + " " + f("H2") + " " + f("H3") +
        " " + f("H4") + " " + f("H5") + f("H6") + "\n  " +
        f("A0") + " " + f("B0") + " " + f("C0") + " " + f("D0") + "\n  " +
        f("A1") + " " + f("B1") + " " + f("C1") + " " + f("D1") + "\n  " +
        f("A2") + " " + f("B2") + " " + f("C2") + " " + f("D2") + "\n  " +
        f("A3") + " " + f("B3") + " " + f("C3") + " " + f("D3") + "\n==========="
    )

def get_current_layout(map: Map) -> str:
    return '_'.join([k + str(v["curr"]) for k,v in sorted(map.items())])

def is_not_trapped(coord: Coord, map: Map) -> bool:
    if coord[0] == "H" or coord[1] == "0":
        return True
    return map[coord[0] + str(int(coord[1]) - 1)]["curr"] is None

def is_moveable(coord: Coord, map: Map) -> bool:
    return not is_at_home(coord, map, map[coord]["curr"]) and is_not_trapped(coord, map)

def get_min_energy(map: Map, min_energy_memo: Dict[str, int]) -> int:
    if (layout := get_current_layout(map)) in min_energy_memo:
        return min_energy_memo[layout]

    min_energy_memo[layout] = float("inf")
    bug_locations: List[Coord] = [coord for coord, data in map.items() if data["curr"] is not None]
    moveable_bug_locations = list(filter(partial(is_moveable, map=map), bug_locations))

    for coord in moveable_bug_locations:
        energy_costs: Dict[Coord, int] = {coord: 0}
        bug_type: BugType = map[coord]["curr"]
        curr_coord = coord

        if curr_coord[0] != "H" and (depth := int(curr_coord[1])) > 0:
            for d in range(depth-1, -1, -1):
                curr_coord: Coord = curr_coord[0] + str(d)                    # Move from deep to shallow
                energy_costs[curr_coord] = STEP_COSTS[bug_type] * (depth - d)

        stack: List[Coord] = [curr_coord]       # Iterative DFS
        while stack:
            curr_coord = stack.pop()

            if is_at_home(curr_coord, map, bug_type):
                new_map = copy.deepcopy(map)
                new_map[curr_coord]["curr"], new_map[coord]["curr"] = new_map[coord]["curr"], None
                min_energy_memo[layout] = energy_costs[curr_coord] + get_min_energy(new_map, min_energy_memo)
                return min_energy_memo[layout]

            for adj_coord, dist in map[curr_coord]["adj"]:
                if (
                    adj_coord in energy_costs or
                    map[adj_coord]["curr"] is not None or
                    adj_coord[0] not in {"H", bug_type}
                ):
                    continue
                energy_costs[adj_coord] = energy_costs[curr_coord] + dist * STEP_COSTS[bug_type]
                stack.append(adj_coord)

        for end_coord, move_energy_cost in energy_costs.items():
            if end_coord[0] != "H" or coord[0] == "H":
                continue
            new_map = copy.deepcopy(map)
            new_map[end_coord]["curr"], new_map[coord]["curr"] = new_map[coord]["curr"], None
            total_energy_cost = move_energy_cost + get_min_energy(new_map, min_energy_memo)
            min_energy_memo[layout] = min(min_energy_memo[layout], total_energy_cost)

    return min_energy_memo[layout]

def get_min_energy_init(inpt: List[str]) -> int:
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
        "A1": {"curr": "D",         "adj": {("A0", 1), ("A2", 1)}},
        "B1": {"curr": "C",         "adj": {("B0", 1), ("B2", 1)}},
        "C1": {"curr": "B",         "adj": {("C0", 1), ("C2", 1)}},
        "D1": {"curr": "A",         "adj": {("D0", 1), ("D2", 1)}},
        "A2": {"curr": "D",         "adj": {("A1", 1), ("A3", 1)}},
        "B2": {"curr": "B",         "adj": {("B1", 1), ("B3", 1)}},
        "C2": {"curr": "A",         "adj": {("C1", 1), ("C3", 1)}},
        "D2": {"curr": "C",         "adj": {("D1", 1), ("D3", 1)}},
        "A3": {"curr": inpt[3][3],  "adj": {("A2", 1)}},
        "B3": {"curr": inpt[3][5],  "adj": {("B2", 1)}},
        "C3": {"curr": inpt[3][7],  "adj": {("C2", 1)}},
        "D3": {"curr": inpt[3][9],  "adj": {("D2", 1)}},
    }
    finished_layout = 'A0A_A1A_A2A_A3A_B0B_B1B_B2B_B3B_C0C_C1C_C2C_C3C_D0D_D1D_D2D_D3D_H0None_H1None_H2None_H3None_H4None_H5None_H6None'
    memo: Dict[str, int] = {finished_layout: 0}
    return get_min_energy(start_map, min_energy_memo=memo)

assert get_min_energy_init(test_input) == 44169
print(get_min_energy_init(full_input))
