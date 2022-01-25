with open("day3.in", "r") as f:
    full_instructions = f.readline()[:-1]


# Part 1

def get_number_of_visited_houses(instructions: str) -> int:
    curr = (0, 0)
    seen = {(0, 0)}
    for instruction in instructions:
        curr = {
            "^": lambda pos: (pos[0], pos[1] + 1),
            "v": lambda pos: (pos[0], pos[1] - 1),
            ">": lambda pos: (pos[0] + 1, pos[1]),
            "<": lambda pos: (pos[0] - 1, pos[1]),
        }[instruction](curr)
        seen.add(curr)
    return len(seen)

assert get_number_of_visited_houses(">") == 2
assert get_number_of_visited_houses("^>v<") == 4
assert get_number_of_visited_houses("^v^v^v^v^v") == 2
print(get_number_of_visited_houses(full_instructions))


# Part 2

def get_number_of_visited_houses_with_robo(instructions: str) -> int:
    curr_mover, alt_mover = (0, 0), (0, 0)
    seen = {(0, 0)}
    for instruction in instructions:
        curr_mover = {
            "^": lambda pos: (pos[0], pos[1] + 1),
            "v": lambda pos: (pos[0], pos[1] - 1),
            ">": lambda pos: (pos[0] + 1, pos[1]),
            "<": lambda pos: (pos[0] - 1, pos[1]),
        }[instruction](curr_mover)
        seen.add(curr_mover)
        curr_mover, alt_mover = alt_mover, curr_mover
    return len(seen)

assert get_number_of_visited_houses_with_robo("^v") == 3
assert get_number_of_visited_houses_with_robo("^>v<") == 3
assert get_number_of_visited_houses_with_robo("^v^v^v^v^v") == 11
print(get_number_of_visited_houses_with_robo(full_instructions))
