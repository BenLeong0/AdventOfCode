import re

WHITESPACE_RE = re.compile(r" +")


def part1(filename: str):
    with open(filename, "r") as f:
        rows = f.read()[:-1]
    seeds_section, *map_sections = rows.split("\n\n")
    seeds = [int(x) for x in seeds_section.split(": ")[1].split(" ")]

    maps = [
        [
            [int(x) for x in mapping.split(" ")]
            for mapping in map_section.split("\n")[1:]
        ]
        for map_section in map_sections
    ]

    curr_lowest = float("inf")
    for seed in seeds:
        for _map in maps:
            for mapping in _map:
                if mapping[1] <= seed < mapping[1] + mapping[2]:
                    seed += mapping[0] - mapping[1]
                    break
        curr_lowest = min(curr_lowest, seed)
    return curr_lowest


def part2(filename: str):
    with open(filename, "r") as f:
        rows = f.read()[:-1]
    seeds_section, *map_sections = rows.split("\n\n")

    maps = [
        [
            [int(x) for x in mapping.split(" ")]
            for mapping in map_section.split("\n")[1:]
        ]
        for map_section in map_sections
    ]

    seed_numbers = [int(x) for x in seeds_section.split(": ")[1].split(" ")]
    curr_seed_ranges = [
        (seed_numbers[i], seed_numbers[i] + seed_numbers[i + 1] - 1)
        for i in range(0, len(seed_numbers), 2)
    ]

    for _map in maps:
        new_seed_ranges = []
        print(curr_seed_ranges)
        print(_map)
        for starting_seed_range in curr_seed_ranges:
            remaining_ranges = [starting_seed_range]
            while remaining_ranges:
                seed_range = remaining_ranges.pop(0)
                for mapping in _map:
                    source_range = (mapping[1], mapping[1] + mapping[2] - 1)
                    d = mapping[0] - mapping[1]
                    if (
                        source_range[0] <= seed_range[0] <= source_range[1] and
                        seed_range[1] > source_range[1]
                    ):
                        new_seed_ranges.append((seed_range[0] + d, source_range[1] + d))
                        remaining_ranges.append((source_range[1] + 1, seed_range[1]))
                        break
                    if (
                        source_range[0] <= seed_range[1] <= source_range[1] and
                        seed_range[0] < source_range[0]
                    ):
                        new_seed_ranges.append((source_range[0] + d, seed_range[1] + d))
                        remaining_ranges.append((seed_range[0], source_range[0] - 1))
                        break
                    if (seed_range[0] >= source_range[0] and seed_range[1] <= source_range[1]):
                        new_seed_ranges.append((seed_range[0] + d, seed_range[1] + d))
                        break
                    if (seed_range[0] <= source_range[0] and seed_range[1] >= source_range[1]):
                        new_seed_ranges.append((source_range[0] + d, source_range[1] + d))
                        remaining_ranges.append((seed_range[0], source_range[0] - 1))
                        remaining_ranges.append((source_range[1], seed_range[1]))
                        break
                else:
                    new_seed_ranges.append(seed_range)
            curr_seed_ranges = new_seed_ranges
    print(curr_seed_ranges)
    return min(map(lambda range: range[0], curr_seed_ranges))


if __name__ == "__main__":
    # res1 = part1("inputs/day05.test.in")
    res1 = part1("inputs/day05.in")
    print(res1)

    # res2 = part2("inputs/day05.test.in")
    res2 = part2("inputs/day05.in")
    print(res2)
