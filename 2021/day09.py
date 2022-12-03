from typing import List, Tuple


test_input: List[int] = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
    [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
]

with open("inputs/day09.in", "r", newline="\n") as readfile:
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


# Part 1
def find_total_risk_level(heights: List[List[int]]) -> int:
    curr_total = 0
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            neighbours = get_neighbours(heights, i, j)
            if all([heights[i][j] < heights[x][y] for x,y in neighbours]):
                curr_total += heights[i][j] + 1
    return curr_total

assert find_total_risk_level(test_input) == 15
print(find_total_risk_level(full_input))


# Part 2
def find_product_of_largest_basins_sizes(heights: List[List[int]]) -> int:
    basin_sizes = []
    seen_points = set()

    # Ignore points with height 9, and don't repeat points
    nb_filter = lambda nb: (nb not in seen_points) and (heights[nb[0]][nb[1]] != 9)

    for i in range(len(heights)):
        for j in range(len(heights[0])):
            if not nb_filter((i,j)):
                continue

            # DFS graph traversal (flood fill)
            curr_basin_size = 0
            stack = [(i,j)]
            seen_points.add((i,j))
            while stack:
                x,y = stack.pop()
                curr_basin_size += 1
                filtered_neighbours = filter(nb_filter, get_neighbours(heights, x, y))
                for neighbour in filtered_neighbours:
                    stack.append(neighbour)
                    seen_points.add(neighbour)
            basin_sizes.append(curr_basin_size)

    sorted_basin_sizes = sorted(basin_sizes, reverse=True)
    return sorted_basin_sizes[0] * sorted_basin_sizes[1] * sorted_basin_sizes[2]

assert find_product_of_largest_basins_sizes(test_input) == 1134
print(find_product_of_largest_basins_sizes(full_input))
