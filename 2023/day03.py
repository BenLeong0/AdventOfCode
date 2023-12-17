from collections import defaultdict
from itertools import product

from utils import file_to_list


def part1(filename: str):
    rows = file_to_list(filename)

    # Pad sides with .'s
    rows = [f".{row}." for row in rows]
    row_length = len(rows[0])
    empty_row = "." * row_length
    rows = [empty_row, *rows, empty_row]
    DIGITS = set('1234567890')

    number_locations: set[tuple[int, int, int]] = set()
    for row_id, row in enumerate(rows):
        curr = None
        for char_id, char in enumerate(row):
            if char not in DIGITS and curr is not None:
                number_locations.add((row_id, curr, char_id - 1))
                curr = None
            if char in DIGITS and curr is None:
                curr = char_id

    NOT_PART = set(".1234567890")
    total = sum(
        int(rows[row_id][char_start:char_end + 1])
        for row_id, char_start, char_end in number_locations
        if any(
            rows[row_id][char_id] not in NOT_PART
            for row_id, char_id in
            product(
                range(row_id - 1, row_id + 2),
                range(char_start -1, char_end + 2)
            )
        )
    )

    return total


def part2(filename: str):
    rows = file_to_list(filename)

    # Pad sides with .'s
    rows = [f".{row}." for row in rows]
    row_length = len(rows[0])
    empty_row = "." * row_length
    rows = [empty_row, *rows, empty_row]
    DIGITS = set('1234567890')

    number_locations: set[tuple[int, int, int]] = set()
    for row_id, row in enumerate(rows):
        curr = None
        for char_id, char in enumerate(row):
            if char not in DIGITS and curr is not None:
                number_locations.add((row_id, curr, char_id - 1))
                curr = None
            if char in DIGITS and curr is None:
                curr = char_id

    gear_locations: defaultdict[tuple[str, str], list[int]] = defaultdict(list)
    for row_id, char_start, char_end in number_locations:
        value = int(rows[row_id][char_start:char_end + 1])
        for row_id, char_id in product(
            range(row_id - 1, row_id + 2),
            range(char_start -1, char_end + 2)
        ):
            if rows[row_id][char_id] == "*":
                gear_locations[(row_id, char_id)].append(value)

    total = 0
    for gear_numbers in gear_locations.values():
        if len(gear_numbers) == 2:
            total += gear_numbers[0] * gear_numbers[1]

    return total


if __name__ == "__main__":
    # res1 = part1("inputs/day03.test.in")
    res1 = part1("inputs/day03.in")
    print(res1)

    # res2 = part2("inputs/day03.test.in")
    res2 = part2("inputs/day03.in")
    print(res2)
