from collections import defaultdict
from typing import Dict


test_template: str = "NNCB"

test_rules: Dict[str, str] = {
    "CH": "B",
    "HH": "N",
    "CB": "H",
    "NH": "C",
    "HB": "C",
    "HC": "B",
    "HN": "C",
    "NN": "C",
    "BH": "H",
    "NC": "B",
    "NB": "B",
    "BN": "B",
    "BB": "N",
    "BC": "B",
    "CC": "N",
    "CN": "C",
}

with open("inputs/day14.in", "r", newline="\n") as readfile:
    file = readfile.read().replace('\r\n', '\n').split('\n\n')
    full_template = file[0].strip()
    full_rules = {x.split(" -> ")[0]:x.split(" -> ")[1] for x in file[1].split("\n")[:-1]}


# Shared
def get_polymer_difference_naive(template: str, rules: Dict[str, str], steps: int = 10):
    for _ in range(steps):
        curr_template = ''
        for i in range(len(template) - 1):
            curr_template += template[i]
            curr_template += rules[template[i:i+2]]
        template = curr_template + template[-1]
    counts = {x: template.count(x) for x in template}
    return max(counts.values()) - min(counts.values())


def get_polymer_difference(template: str, rules: Dict[str, str], steps: int = 10):
    pairs = defaultdict(int)
    for i in range(len(template)-1):
        pairs[template[i:i+2]] += 1

    for _ in range(steps):
        curr_pairs = defaultdict(int)
        for pair, pair_count in pairs.items():
            curr_pairs[pair[0]+rules[pair]] += pair_count
            curr_pairs[rules[pair]+pair[1]] += pair_count
        pairs = curr_pairs

    counts = defaultdict(int, {template[0]: 0.5, template[-1]: 0.5})
    for pair, pair_count in pairs.items():
        counts[pair[0]] += pair_count / 2  # A single char will show up in two pairs, so half the count
        counts[pair[1]] += pair_count / 2

    return int(max(counts.values()) - min(counts.values()))


# Part 1
assert get_polymer_difference(test_template, test_rules) == 1588
print(get_polymer_difference(full_template, full_rules))

# Part 2
assert get_polymer_difference(test_template, test_rules, steps=40) == 2188189693529
print(get_polymer_difference(full_template, full_rules, steps=40))

