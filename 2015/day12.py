import json
import re

with open('inputs/day12.in', "r", newline="") as f:
    full_json = f.readline()


# Part 1

def get_total_sum(json_string: str) -> int:
    return sum([int(x) for x in re.findall(r"-?\d+", json_string)])


# Part 2

def get_non_red_total_sum(json_string: str) -> int:
    accounts = json.loads(json_string)
    def get_recursive_sum(obj: int | list | dict[str, str | int | list | dict]) -> int:
        if isinstance(obj, int):
            return obj
        if isinstance(obj, list):
            return sum([get_recursive_sum(v) for v in obj])
        if isinstance(obj, str) or "red" in obj.values():
            return 0
        return sum([get_recursive_sum(v) for v in obj.values()])
    return get_recursive_sum(accounts)

print(get_non_red_total_sum(full_json))
