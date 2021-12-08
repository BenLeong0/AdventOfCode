from typing import List


test_input: List[int] = [16,1,2,0,4,2,7,1,2,14]

with open("day7.in", "r", newline="\n") as readfile:
    full_input = [int(x) for x in readfile.readline()[:-1].split(',')]


# Part 1
def find_min_fuel(starting_positions: List[int]) -> int:
    sorted_positions = sorted(starting_positions)
    curr_min = float("inf")
    for pos in range(sorted_positions[-1] + 1):
        fuel_usage = sum([abs(x-pos) for x in sorted_positions])
        curr_min = min(curr_min, fuel_usage)
    return curr_min

assert find_min_fuel(test_input) == 37
print(find_min_fuel(full_input))


# Part 2
def find_min_fuel_exponential(starting_positions: List[int]) -> int:
    triangle_number = lambda n: (n*(n+1))//2
    sorted_positions = sorted(starting_positions)
    curr_min = float("inf")
    for pos in range(sorted_positions[-1] + 1):
        fuel_usage = sum([triangle_number(abs(x-pos)) for x in sorted_positions])
        curr_min = min(curr_min, fuel_usage)
    return curr_min

assert find_min_fuel_exponential(test_input) == 168
print(find_min_fuel_exponential(full_input))
