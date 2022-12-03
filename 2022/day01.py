from itertools import combinations


INPUT_FILE = "inputs/day01.in"

part1 = max(sum(map(int, x.split("\n"))) for x in open(INPUT_FILE).read().split("\n\n"))
part2 = max(sum(y) for y in combinations((sum(map(int, x.split("\n"))) for x in open(INPUT_FILE).read().split("\n\n")), r=3))

print(part1)
print(part2)


######

from utils import file_to_list


def part2optimal(filename: str) -> int:
    """boooo; O(n) solution (but BORING)"""
    top_three = []
    curr_sum = 0
    rows = file_to_list(filename)
    for row in rows:
        if row != "":
            curr_sum += int(row)
        else:
            top_three.append(curr_sum)
            curr_sum = 0
        if len(top_three) > 3:
            top_three.remove(min(top_three))
    return sum(top_three)


print(part2optimal(INPUT_FILE))
