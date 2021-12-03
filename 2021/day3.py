import copy
from typing import List


test_input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

with open("day3.in", "r", newline="\n") as readfile:
    full_input = [x[:-1] for x in readfile.readlines()]


# Shared
def get_most_common_bit(rows: List[str], index: int) -> str:
    col = [row[index] for row in rows]
    return '1' if col.count('1') >= col.count('0') else '0'


# Part 1
def power_consumption(report: List[str]) -> int:
    row_length = len(report[0])

    gamma_bin = [get_most_common_bit(report, i) for i in range(row_length)]

    gamma = int(''.join(gamma_bin), 2)
    epsilon = 2**len(report[0]) - 1 - gamma

    return gamma * epsilon

assert power_consumption(test_input) == 198
print(power_consumption(full_input))


# Part 2
def life_support_rating(report: List[str]) -> int:
    row_length = len(report[0])

    def get_most_common_bit(rows: List[str], index: int) -> str:
        col = [row[index] for row in rows]
        return '1' if col.count('1') >= col.count('0') else '0'

    oxygen_rows = copy.deepcopy(report)
    for i in range(row_length):
        if len(oxygen_rows) == 1:
            break
        oxygen_rows = list(filter(lambda x: x[i]==get_most_common_bit(oxygen_rows, i), oxygen_rows))
    oxygen_rating = int(''.join(oxygen_rows[0]), 2)

    co2_rows = copy.deepcopy(report)
    for i in range(row_length):
        if len(co2_rows) == 1:
            break
        co2_rows = list(filter(lambda x: x[i]!=get_most_common_bit(co2_rows, i), co2_rows))
    co2_rating = int(''.join(co2_rows[0]), 2)

    return oxygen_rating * co2_rating


assert life_support_rating(test_input) == 230
print(life_support_rating(full_input))