from functools import cmp_to_key
from itertools import combinations
from utils import file_to_list

INPUT_FILE_TEST = "inputs/day05.test.in"
INPUT_FILE = "inputs/day05.in"


def part1(filename: str) -> int:
    rows = file_to_list(filename)

    split_index = rows.index("")
    rules = set(
        (int(x.split("|")[0]), int(x.split("|")[1])) for x in rows[:split_index]
    )
    updates = rows[split_index + 1 :]
    valid_updates: list[list[int]] = []
    for update_row in updates:
        update = [int(x) for x in update_row.split(",")]
        if _is_update_valid(update, rules):
            valid_updates.append(update)

    middle_pages = [
        valid_update[len(valid_update) // 2] for valid_update in valid_updates
    ]
    return sum(middle_pages)


def _is_update_valid(update: list[int], rules: set[tuple[int, int]]) -> bool:
    return all(
        (update[j], update[i]) not in rules
        for i, j in combinations(range(len(update)), 2)
    )


print(part1(INPUT_FILE_TEST))
print(part1(INPUT_FILE))


def part2(filename: str) -> int:
    rows = file_to_list(filename)

    split_index = rows.index("")
    rules = set(
        (int(x.split("|")[0]), int(x.split("|")[1])) for x in rows[:split_index]
    )

    def sorting_key(x: int, y: int):
        return -1 if (x, y) in rules else 1

    updates = rows[split_index + 1 :]
    invalid_updates: list[list[int]] = []
    for update_row in updates:
        update = [int(x) for x in update_row.split(",")]
        if not _is_update_valid(update, rules):
            invalid_updates.append(update)

    sorted_invalid_updates = [
        sorted(invalid_update, key=cmp_to_key(sorting_key))
        for invalid_update in invalid_updates
    ]
    middle_pages = [
        invalid_update[len(invalid_update) // 2]
        for invalid_update in sorted_invalid_updates
    ]
    return sum(middle_pages)


print(part2(INPUT_FILE_TEST))
print(part2(INPUT_FILE))
