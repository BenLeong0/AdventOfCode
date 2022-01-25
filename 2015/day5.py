import re
from typing import List


with open("day5.in", "r", newline="") as readfile:
    full_input = list(readfile.readlines())


# Part 1

def is_nice_old(s: str) -> bool:
    return (
        len(re.findall(r"[aeiou]", s)) >= 3 and
        re.search(r"(.)\1", s) is not None and
        re.search(r"ab|cd|pq|xy", s) is None
    )

def count_nice_strings_old(strings: List[str]) -> int:
    return len(list(filter(is_nice_old, strings)))

assert is_nice_old("ugknbfddgicrmopn") is True
assert is_nice_old("aaa") is True
assert is_nice_old("jchzalrnumimnmhp") is False
assert is_nice_old("haegwjzuvuyypxyu") is False
assert is_nice_old("dvszwmarrgswjxmb") is False
print(count_nice_strings_old(full_input))


# Part 2

def is_nice_new(s: str) -> bool:
    return (
        re.search(r"(..).*\1", s) is not None and
        re.search(r"(.).\1", s) is not None
    )

def count_nice_strings_new(strings: List[str]) -> int:
    return len(list(filter(is_nice_new, strings)))

assert is_nice_new("qjhvhtzxzqqjkmpb") is True
assert is_nice_new("xxyxx") is True
assert is_nice_new("uurcxstgmygtbstg") is False
assert is_nice_new("ieodomkazucvgmuy") is False
print(count_nice_strings_new(full_input))
