from itertools import product


test_containers = [20, 15, 10, 5, 5]
full_containers = [11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]


# Part 1

def get_number_of_combinations(containers: list[int], size: int) -> int:
    return sum([
        size == sum([x*y for x,y in zip(containers, truth_values)])
        for truth_values in product((0, 1), repeat=len(containers))
    ])

assert get_number_of_combinations(test_containers, 25) == 4
print(get_number_of_combinations(full_containers, 150))


# Part 2

def get_min_number_of_containers(containers: list[int], size: int) -> int:
    return min([
        sum(truth_values)
        for truth_values in product((0, 1), repeat=len(containers))
        if size == sum([x*y for x,y in zip(containers, truth_values)])
    ])

assert get_min_number_of_containers(test_containers, 25) == 2
print(get_min_number_of_containers(full_containers, 150))
