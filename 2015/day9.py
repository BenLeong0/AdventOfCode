from collections import defaultdict
from typing import DefaultDict, List, Tuple

Location = str
Route = Tuple[Location, Location, int]

test_routes: List[Route] = [
    ("London", "Dublin", 464),
    ("London", "Belfast", 518),
    ("Dublin", "Belfast", 141),
]

with open("day9.in", "r", newline="") as readfile:
    full_routes: List[Route] = [
        (route[0], route[2], int(route[4]))
        for route in [x.split() for x in readfile.readlines()]
    ]

# Shared

def build_adj_dict(routes: List[Route]) -> dict[Location, dict[Location, int]]:
    adj_dict: DefaultDict[Location, dict[Location, int]] = defaultdict(lambda : {})
    for route in routes:
        adj_dict[route[0]][route[1]] = route[2]
        adj_dict[route[1]][route[0]] = route[2]
    adj_dict["Start"] = {location:0 for location in adj_dict}
    return dict(adj_dict)


# Part 1

def find_shortest_route_recursive(routes: List[Route]) -> int:
    adj_dict = build_adj_dict(routes)
    seen = set()
    def dfs(location: Location) -> int:
        seen.add(location)
        min_dist = min([
            adj_dict[location][destination] + dfs(destination)
            for destination in adj_dict[location]
            if destination not in seen
        ], default=0)
        seen.remove(location)
        return min_dist
    return dfs("Start")

assert find_shortest_route_recursive(test_routes) == 605
print(find_shortest_route_recursive(full_routes))


# Part 2

def find_longest_route_recursive(routes: List[Route]) -> int:
    adj_dict = build_adj_dict(routes)
    seen = set()
    def dfs(location: Location) -> int:
        seen.add(location)
        min_dist = max([
            adj_dict[location][destination] + dfs(destination)
            for destination in adj_dict[location]
            if destination not in seen
        ], default=0)
        seen.remove(location)
        return min_dist
    return dfs("Start")

assert find_longest_route_recursive(test_routes) == 982
print(find_longest_route_recursive(full_routes))
