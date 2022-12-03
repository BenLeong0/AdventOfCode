import re
from typing import List

test_input = [
    r'""',
    r'"abc"',
    r'"aaa\"aaa"',
    r'"\x27"',
]


with open('inputs/day08.in', newline="") as readfile:
    full_input = list(readfile.readlines())


# Part 1

def get_decoded_character_difference(string_list: List[str]) -> int:
    return sum([len(s) - len(re.sub(r"\\\\|\\\"|\\x[\da-f]{2}", "x", s[1:-1])) for s in string_list])
    # return sum([2 + len(re.findall(r"\\\\|\\\"", s)) + 3 * len(re.findall(r"\\x[\da-f]{2}", s)) for s in string_list])

assert get_decoded_character_difference(test_input) == 12
print(get_decoded_character_difference(full_input))


# Part 2

def get_encoded_character_difference(string_list: List[str]) -> int:
    return sum([2 + len(re.findall(r"\\|\"", s)) for s in string_list])

assert get_encoded_character_difference(test_input) == 19
print(get_encoded_character_difference(full_input))
