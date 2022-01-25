from functools import reduce
from typing import List, Tuple


Lengths = Tuple[int, int, int]


test_lengths: List[Lengths] = [(2,3,4), (1,1,10)]

with open("day2.in", "r") as readfile:
    full_input = [x[:-1] for x in readfile.readlines()]
    full_lengths = [tuple(map(int, x.split("x"))) for x in full_input]



# Part 1

def get_total_paper_required(all_lengths: List[Lengths]) -> int:
    def get_paper_required(lengths: Lengths) -> int:
        sides = [lengths[i%3] * lengths[(i+1)%3] for i in range(3)]
        return 2 * sum(sides) + min(sides)
    return sum(map(get_paper_required, all_lengths))


assert get_total_paper_required(test_lengths) == 58 + 43
print(get_total_paper_required(full_lengths))


# Part 2

def get_total_ribbon_length_required(all_lengths: List[Lengths]) -> int:
    def get_ribbon_required(lengths: Lengths) -> int:
        sorted_lengths = sorted(lengths)
        return 2 * (sorted_lengths[0] + sorted_lengths[1]) + reduce(lambda x,y:x*y, lengths)
    return sum(map(get_ribbon_required, all_lengths))


assert get_total_ribbon_length_required(test_lengths) == 34 + 14
print(get_total_ribbon_length_required(full_lengths))
