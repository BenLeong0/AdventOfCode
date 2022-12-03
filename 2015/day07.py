from typing import Dict, Literal, Tuple, Union


Operation = Literal["AND", "OR", "LSHIFT", "RSHIFT", "NOT", "IS"]
Wire = str
Instruction = Tuple[Operation, Union[Wire, Tuple[Wire, Wire]]]

with open('inputs/day07.in', newline="") as readfile:
    dependency_dict: Dict[Wire, Instruction] = {}
    for instruction in [x.split() for x in readfile.readlines()]:
        if instruction[0] == "NOT":
            dependency_dict[instruction[-1]] = ("NOT", instruction[1])
        elif instruction[1] in ("AND", "OR", "LSHIFT", "RSHIFT"):
            dependency_dict[instruction[-1]] = (instruction[1], (instruction[0], instruction[2]))
        else:
            dependency_dict[instruction[-1]] = ("IS", instruction[0])


# Shared

cache: Dict[Wire, int] = {}
def get_signal(wire: Wire) -> int:
    if wire.isdigit():
        return int(wire)
    instruction = dependency_dict[wire]
    if wire not in cache:
        cache[wire] = {
            "IS"     : lambda x: get_signal(x),
            "NOT"    : lambda x: 65535 - get_signal(x),
            "AND"    : lambda x: get_signal(x[0]) & get_signal(x[1]),
            "OR"     : lambda x: get_signal(x[0]) | get_signal(x[1]),
            "LSHIFT" : lambda x: get_signal(x[0]) << get_signal(x[1]),
            "RSHIFT" : lambda x: get_signal(x[0]) >> get_signal(x[1]),
        }[instruction[0]](instruction[1])
    return cache[wire]


# Part 1
print(get_signal("a"))

# Part 2
dependency_dict["b"] = ("IS", str(get_signal("a")))
cache.clear()
print(get_signal("a"))
