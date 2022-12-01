with open("day1.in", "r", newline="") as f:
    full_instructions = f.readline()


# Part 1

def get_final_floor(instructions: str) -> int:
    return sum([1 if char == "(" else -1 for char in instructions])

assert get_final_floor("(())") == 0
assert get_final_floor("))(((((") == 3
print(get_final_floor(full_instructions))


# Part 2

def get_first_basement_entry(instructions: str) -> int:
    curr_floor = 0
    for (i, char) in enumerate(instructions, start=1):
        curr_floor += 1 if char == "(" else -1
        if curr_floor == -1:
            return i

assert get_first_basement_entry(")") == 1
assert get_first_basement_entry("()())") == 5
print(get_first_basement_entry(full_instructions))
