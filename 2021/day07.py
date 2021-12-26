from typing import List


test_input: List[int] = [16,1,2,0,4,2,7,1,2,14]

with open("input_files/day07.in", "r", newline="\n") as readfile:
    full_input = [int(x) for x in readfile.readline()[:-1].split(',')]


# Part 1
def find_min_fuel(starting_positions: List[int]) -> int:
    sorted_positions = sorted(starting_positions)

    def get_total_fuel_usage(pos: int) -> int:
        return sum([abs(x-pos) for x in sorted_positions])

    return min([get_total_fuel_usage(pos) for pos in range(sorted_positions[-1] + 1)])

assert find_min_fuel(test_input) == 37
print(find_min_fuel(full_input))


# Part 2
def find_min_fuel_exponential(starting_positions: List[int]) -> int:
    sorted_positions = sorted(starting_positions)

    def get_triangle_number(n: int) -> int:
        return ((n) * (n + 1)) // 2

    def get_total_fuel_usage(pos: int) -> int:
        return sum([get_triangle_number(abs(x-pos)) for x in sorted_positions])

    return min([get_total_fuel_usage(pos) for pos in range(sorted_positions[-1] + 1)])

assert find_min_fuel_exponential(test_input) == 168
print(find_min_fuel_exponential(full_input))
