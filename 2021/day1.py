from typing import List


test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

with open("day1.in", "r") as readfile:
    full_input = [int(x) for x in readfile.readlines()]


# Part 1
def count_increases(depths: List[int]) -> int:
    if len(depths) == 0:
        return 0

    curr_depth = depths[0]
    count = 0

    for depth in depths[1:]:
        if depth > curr_depth:
            count += 1
        curr_depth = depth

    return count

assert count_increases(test_input) == 7
print(count_increases(full_input))


# Part 2
def sliding_window_increases(depths: List[int]) -> int:
    if len(depths) < 3:
        return 0

    count = 0

    def compare_to_previous_window(index: int) -> bool:
        return sum(depths[index:index+3]) > sum(depths[index-1:index+2])

    for i in range(1, len(depths) - 2):
        if compare_to_previous_window(i):
            count += 1

    return count

assert sliding_window_increases(test_input) == 5
print(sliding_window_increases(full_input))
