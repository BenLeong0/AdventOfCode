import re

from utils import file_to_list

INPUT_FILE = "inputs/day01.in"

FIRST_DIGIT_RE = re.compile(r"^\D*(\d).*$")
SECOND_DIGIT_RE = re.compile(r"^.*(\d)\D*$")

def part1(filename: str) -> int:
    rows = file_to_list(filename)
    total = 0
    for row in rows:
        first_digit = FIRST_DIGIT_RE.match(row).group(1)
        second_digit = SECOND_DIGIT_RE.match(row).group(1)
        total += int(first_digit + second_digit)
    return total

print(part1(INPUT_FILE))

NUMBER_WORDS = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
}

def part1(filename: str) -> int:
    rows = file_to_list(filename)
    total = 0
    for row in rows:
        first = get_first(row)
        print(first)

        last = get_last(row)
        print(last)
        total += int(first + last)

    return total

def get_first(row):
    for i in range(len(row)):
        for num in NUMBER_WORDS:
            if row[i:i+len(num)] == num:
                return NUMBER_WORDS[num]

def get_last(row):
    for i in range(len(row)-1, -1, -1):
        for num in NUMBER_WORDS:
            if row[i:i+len(num)] == num:
                return NUMBER_WORDS[num]

print(part1(INPUT_FILE))
