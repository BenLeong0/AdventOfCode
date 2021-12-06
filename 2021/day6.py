import copy
from typing import List


test_input: List[int] = [3,4,3,1,2]

with open("day6.in", "r", newline="\n") as readfile:
    full_input = [int(x) for x in readfile.readline()[:-1].split(',')]


# Part 1
def find_number_of_lanternfish_old(lantern_fish_timers: List[int], num_days: int=80) -> int:
    for _ in range(num_days):
        new_fish = 0
        for (i, timer) in enumerate(lantern_fish_timers):
            if timer == 0:
                lantern_fish_timers[i] = 6
                new_fish += 1
            else:
                lantern_fish_timers[i] -= 1

        lantern_fish_timers += [8 for __ in range(new_fish)]

    return len(lantern_fish_timers)


def find_number_of_lanternfish(lantern_fish_timers: List[int], num_days: int=80) -> int:
    num_of_fish = [lantern_fish_timers.count(i) for i in range(9)]
    for _ in range(num_days):
        num_of_fish = [
            num_of_fish[1],
            num_of_fish[2],
            num_of_fish[3],
            num_of_fish[4],
            num_of_fish[5],
            num_of_fish[6],
            num_of_fish[7] + num_of_fish[0],    # All ex-age 7 + new parents
            num_of_fish[8],
            num_of_fish[0],                     # All new children
        ]

    return sum(num_of_fish)


assert find_number_of_lanternfish(copy.deepcopy(test_input), 18) == 26
assert find_number_of_lanternfish(copy.deepcopy(test_input)) == 5934
print(find_number_of_lanternfish(copy.deepcopy(full_input)))


# Part 2
assert find_number_of_lanternfish(copy.deepcopy(test_input), 256) == 26984457539
print(find_number_of_lanternfish(copy.deepcopy(full_input), 256))
