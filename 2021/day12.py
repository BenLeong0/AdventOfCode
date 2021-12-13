from collections import defaultdict
from typing import DefaultDict, Dict, List, Tuple

from day12_input import *


# Shared
def build_adj_dict(edges: List[Tuple[str, str]]) -> Dict[str, List[str]]:
    adj_dict: DefaultDict[str, List[str]] = defaultdict(list)
    for edge in edges:
        adj_dict[edge[0]].append(edge[1])
        adj_dict[edge[1]].append(edge[0])
    return dict(adj_dict)


# Part 1
def get_number_of_routes(edges: List[Tuple[str, str]]) -> int:
    adj_dict = build_adj_dict(edges)

    def get_number_of_routes_from_point(curr_path: List[str]) -> int:
        if curr_path[-1] == "end":
            return 1

        num_of_routes = 0
        neighbours = adj_dict[curr_path[-1]]
        for neighbour in filter(lambda x: x.isupper() or not x in curr_path, neighbours):
            num_of_routes += get_number_of_routes_from_point(curr_path + [neighbour])

        return num_of_routes

    return get_number_of_routes_from_point(["start"])

assert get_number_of_routes(test_input1) == 10
assert get_number_of_routes(test_input2) == 19
assert get_number_of_routes(test_input3) == 226
print(get_number_of_routes(full_input))


# Part 2
def get_number_of_routes(edges: List[Tuple[str, str]]) -> int:
    adj_dict = build_adj_dict(edges)

    def get_number_of_routes_from_point(curr_path: List[str], revisited: bool = False) -> int:
        if curr_path[-1] == "end":
            return 1

        num_of_routes = 0
        neighbours = adj_dict[curr_path[-1]]
        for nb in neighbours:
            if nb.islower() and curr_path.count(nb) > 1 or nb == "start":
                continue
            elif nb.isupper() or curr_path.count(nb) == 0:
                num_of_routes += get_number_of_routes_from_point(curr_path+[nb], revisited=revisited)
            elif curr_path.count(nb) == 1 and revisited is False:
                num_of_routes += get_number_of_routes_from_point(curr_path+[nb], revisited=True)
        return num_of_routes

    return get_number_of_routes_from_point(["start"])

assert get_number_of_routes(test_input1) == 36
assert get_number_of_routes(test_input2) == 103
assert get_number_of_routes(test_input3) == 3509
print(get_number_of_routes(full_input))
