from utils import file_to_list

INPUT_FILE_TEST = "inputs/day07.test.in"
INPUT_FILE = "inputs/day07.in"


def part1(filename: str) -> int:
    rows = file_to_list(filename)
    equations = [
        (
            int(split_row[0]),
            [int(n) for n in split_row[1].split()],
        )
        for row in rows
        if (split_row := row.split(": "))
    ]

    return sum(equation[0] for equation in equations if is_possible_p1(*equation))


def is_possible_p1(target: int, values: list[int]) -> bool:
    if len(values) == 1:
        return values[0] == target

    [*new_values, n] = values
    return (
        target % n == 0
        and is_possible_p1(target // n, new_values)
        or target > n
        and is_possible_p1(target - n, new_values)
    )


print(part1(INPUT_FILE_TEST))
print(part1(INPUT_FILE))


def part2(filename: str) -> int:
    rows = file_to_list(filename)
    equations = [
        (
            int(split_row[0]),
            [int(n) for n in split_row[1].split()],
        )
        for row in rows
        if (split_row := row.split(": "))
    ]

    return sum(
        equation[0]
        for equation in equations
        if any(equation[0] == option for option in get_all_options(equation[1]))
    )


def get_all_options(values: list[int]) -> list[int]:
    if len(values) == 1:
        return [values[0]]

    return [
        *get_all_options([values[0] * values[1], *values[2:]]),
        *get_all_options([values[0] + values[1], *values[2:]]),
        *get_all_options([int(str(values[0]) + str(values[1])), *values[2:]]),
    ]


print(part2(INPUT_FILE_TEST))
print(part2(INPUT_FILE))
