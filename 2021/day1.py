from typing import List


test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

with open("day1.in", "r") as readfile:
    full_input = [int(x) for x in readfile.readlines()]


# Part 1
def count_increases(depths: List[int]) -> int:
    return sum([depths[i]<depths[i+1] for i in range(len(depths)-1)])

assert count_increases(test_input) == 7
print(count_increases(full_input))


# Part 2
def sliding_window_increases(depths: List[int]) -> int:
    return sum([sum(depths[i:i+3])<sum(depths[i+1:i+4]) for i in range(len(depths)-2)])

assert sliding_window_increases(test_input) == 5
print(sliding_window_increases(full_input))
