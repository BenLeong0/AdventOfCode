from typing import List, Tuple


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

with open("day9.in", "r", newline="\n") as readfile:
    full_input = [[int(x) for x in line[:-1]] for line in readfile.readlines()]


# Shared
def get_neighbours(heights: List[List[int]], i: int, j: int) -> List[Tuple[int, int]]:
    length = len(heights)
    width = len(heights[0])
    neighbours = []
    if i > 0:
        neighbours.append((i-1, j))
    if i < length - 1:
        neighbours.append((i+1, j))
    if j > 0:
        neighbours.append((i, j-1))
    if j < width - 1:
        neighbours.append((i, j+1))
    return neighbours


def dijkstras(graph: List[List[int]]) -> int:
    height, width = len(graph), len(graph[0])
    distances = {(i,j):float('inf') for i in range(height) for j in range(width)}
    unvisited = set(distances.keys())
    def nodeNotVisited(node: Tuple[int, int]):
        return node in unvisited
    
    curr_node = (0, 0)
    distances[curr_node] = 0
    while (height-1, width-1) in unvisited:
        for (x,y) in get_neighbours(graph, *curr_node):
            distances[(x,y)] = min(distances[curr_node] + graph[x][y], distances[(x,y)])
        unvisited.remove(curr_node)
        curr_node = min(filter(nodeNotVisited, distances), key=lambda node: distances[node])
    
    return distances[(height-1, width-1)]


# Part 1
assert dijkstras(test_input) == 40
print(dijkstras(full_input))