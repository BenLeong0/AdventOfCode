from typing import Callable, TypedDict


class Aunt(TypedDict, total=False):
    children: int
    cats: int
    samoyeds: int
    pomeranians: int
    akitas: int
    vizslas: int
    goldfish: int
    trees: int
    cars: int
    perfumes: int


with open("day16.in", "r", newline="") as readfile:
    full_aunt_list: list[Aunt] = {
        int(aunt[1][:-1]): {
            aunt[2][:-1]: int(aunt[3][:-1]),
            aunt[4][:-1]: int(aunt[5][:-1]),
            aunt[6][:-1]: int(aunt[7]),
        }
        for aunt in [x.split() for x in readfile.readlines()]
    }

expected_values: Aunt = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


# Part 1

def get_true_aunt(aunt_list: list[Aunt]):
    for aunt_number, aunt_info in aunt_list.items():
        if all([aunt_info[k] == expected_values[k] for k in aunt_info]):
            return aunt_number

print(get_true_aunt(full_aunt_list))


# Part 2

def get_true_aunt(aunt_list: list[Aunt]):
    checks: dict[str, Callable[[int, int], bool]] = {
        "cats": lambda x, y: x > y,
        "trees": lambda x, y: x > y,
        "pomeranians": lambda x, y: x < y,
        "goldfish": lambda x, y: x < y,
    }
    for aunt_number, aunt_info in aunt_list.items():
        if all([
            checks.get(k, lambda x, y: x==y)(aunt_info[k], expected_values[k]) for k in aunt_info
        ]):
            return aunt_number

print(get_true_aunt(full_aunt_list))
