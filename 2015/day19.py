import re
from typing import List, Set, Tuple


Replacement = Tuple[str, str]

test_replacements: List[Replacement] = [
    ("e", "H"),
    ("e", "O"),
    ("H", "HO"),
    ("H", "OH"),
    ("O", "HH"),
]


with open("day19.in", "r", newline="") as readfile:
    full_input: List[str] = [row for row in readfile.readlines()]
    full_replacements = [(x[0], x[2]) for x in [y.split() for y in full_input[:-2]]]
    full_start_mol = full_input[-1]


# Part 1

def get_number_of_molecules(start_molecule: str, replacement_list: List[Replacement]) -> int:
    possible_results: Set[str] = set()
    for replacement in replacement_list:
        possible_results.update({
            start_molecule[:match.span()[0]] + replacement[1] + start_molecule[match.span()[1]:]
            for match in re.finditer(replacement[0], start_molecule)
        })
    return len(possible_results)

assert get_number_of_molecules("HOH", test_replacements) == 4
assert get_number_of_molecules("HOHOHO", test_replacements) == 7
print(get_number_of_molecules(full_start_mol, full_replacements))


# Part 2

def get_possible_predecessors(curr_molecule: str, replacement_list: List[Replacement]) -> Set[str]:
    possible_predecessors: Set[str] = set()
    for replacement in replacement_list:
        possible_predecessors.update({
            curr_molecule[:match.span()[0]] + replacement[0] + curr_molecule[match.span()[1]:]
            for match in re.finditer(replacement[1], curr_molecule)
        })
    return {p for p in possible_predecessors if len(p) == 1 or "e" not in p}


def get_min_generation_steps(target_molecule: str, replacement_list: List[Replacement]) -> int:
    sorted_replacement_list = sorted(replacement_list, key=lambda x:len(x[1])-len(x[0]), reverse=True)
    print(sorted_replacement_list)
    def dfs(curr_mol: str) -> int:
        if curr_mol == "e":
            return 0
        for predecessor in get_possible_predecessors(curr_mol, sorted_replacement_list):
            if (dist := dfs(predecessor)) < float("inf"):
                return 1 + dist
        return float("inf")
    return dfs(target_molecule)

print(get_min_generation_steps("HOH", test_replacements))
assert get_min_generation_steps("HOH", test_replacements) == 3
assert get_min_generation_steps("HOHOHO", test_replacements) == 6
print(get_min_generation_steps(full_start_mol, full_replacements))

