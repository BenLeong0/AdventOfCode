from typing import List


def file_to_list(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return list(f.read().splitlines())