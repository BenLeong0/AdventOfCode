# Part 1 and 2

def look_and_say(start_sequence: str, iterations: int = 40) -> int:
    sequence = start_sequence
    for _ in range(iterations):
        new_sequence = ''
        curr_char, curr_count = sequence[0], 1
        for char in sequence[1:]:
            if char == curr_char:
                curr_count += 1
            else:
                new_sequence += str(curr_count) + curr_char
                curr_char, curr_count = char, 1
        new_sequence += str(curr_count) + curr_char
        sequence = new_sequence
    return len(sequence)

assert look_and_say("1", 5) == 6
print(look_and_say("1321131112"))
print(look_and_say("1321131112", 50))
