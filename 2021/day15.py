import copy
from typing import Dict, List, Set, Tuple


test_input: List[List[int]] = [
    [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
    [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
    [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
    [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
    [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
    [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
    [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
    [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
    [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
    [2, 3, 1, 1, 9, 4, 4, 5, 8, 1],
]

# Project Euler question 83 is identical, so also tested here
euler_test_input = [
    [131,673,234,103,18],
    [201,96,342,965,150],
    [630,803,746,422,111],
    [537,699,497,121,956],
    [805,732,524,37,331]
]

with open("inputs/day15.in", "r", newline="\n") as readfile:
    full_input = [[int(x) for x in line[:-1]] for line in readfile.readlines()]

with open("inputs/day15euler.in", "r", newline="\n") as readfile:
    euler_full_input = [[int(x) for x in line.split(",")] for line in readfile.readlines()]


# Shared
def get_neighbours(graph: List[List[int]], x_coord: int, y_coord: int) -> List[Tuple[int, int]]:
    return [
        (x_coord + i, y_coord + j) for i in (-1, 0, 1) for j in (-1, 0, 1)
        if abs(i) != abs(j) and 0 <= x_coord+i < len(graph) and 0 <= y_coord+j < len(graph[0])
    ]


# Part 1
def find_lowest_risk(graph: List[List[int]]) -> int:
    height, width = len(graph), len(graph[0])
    distances: Dict[Tuple[int,int],int] = {(0,0): 0}
    visited: Set[Tuple[int,int]] = set()

    def nodeNotVisited(node: Tuple[int, int]) -> bool:
        return node not in visited
    def nodeNotSeenOrVisited(node: Tuple[int, int]) -> bool:
        return node not in visited and node not in distances

    distances[(0, 0)] = 0
    while (height-1, width-1) not in distances:
        curr_node = min(filter(nodeNotVisited, distances), key=lambda node: distances[node])
        for (x,y) in filter(nodeNotSeenOrVisited, get_neighbours(graph, *curr_node)):
            distances[(x,y)] = distances[curr_node] + graph[x][y]
        visited.add(curr_node)
        del distances[curr_node]

    return distances[(height-1, width-1)]

assert find_lowest_risk(test_input) == 40
print(find_lowest_risk(full_input))

assert find_lowest_risk(euler_test_input) + euler_test_input[0][0] == 2297
print(find_lowest_risk(euler_full_input) + euler_full_input[0][0])


# Part 2
def increment_grid(graph: List[List[int]], increase_by: int) -> List[List[int]]:
    new_graph = copy.deepcopy(graph)
    for row_i, entry in enumerate(new_graph):
        for col_i, value in enumerate(entry):
            new_graph[row_i][col_i] = ((value + increase_by - 1) % 9) + 1
    return new_graph


def find_lowest_risk_tiled(graph: List[List[int]]) -> int:
    tiles = [[increment_grid(graph, i+j) for j in range(5)] for i in range(5)]
    full_map = []
    for row_of_tiles in tiles:
        for i in range(len(row_of_tiles[0])):
            curr_row = []
            for tile in row_of_tiles:
                curr_row += tile[i]
            full_map.append(curr_row)

    return find_lowest_risk(full_map)

assert find_lowest_risk_tiled(test_input) == 315
print(find_lowest_risk_tiled(full_input))
