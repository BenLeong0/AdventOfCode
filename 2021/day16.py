from typing import List, Tuple


test_input: str = "D2FE28"

with open("day16.in", "r", newline="\n") as readfile:
    full_input = readfile.readline()[:-1]

# V = 110 = 6 = version
# type = 100 = 4 => literal
# next 5 = 1 0111 (start with 1 => continue) => 0111
# next 5 = 1 1110 (start with 1 => continue) => 01111110
# next 5 = 0 0101 (start with 0 => final group) => 011111100101 = 2021
# last 3 = 000 = all 0 => ignore
# => value =

# Part 1
def get_packet_info(hex_input: str) -> Tuple[int,int]:
    """Return tuple of (version sum, packet length)"""
    binary_rep = bin(int(hex_input, 16))[2:].zfill(4*len(hex_input)).rstrip("0")
    version = int(binary_rep[0:3], 2)
    type_id = int(binary_rep[3:6], 2)

    if type_id == 4:
        curr_num = ''
        i = 6
        while True:
            curr_packet = binary_rep[i:i+5]
            curr_num += curr_packet[1:]
            if curr_packet[0] == '0':
                break
            i += 5
        return version, i

    else:
        length_type_id = binary_rep[6]
        if length_type_id == '0':
            length = int(binary_rep[7:22])
            i = 6
            while i < length+6:
                new_version, new_length = get_packet_info(hex_input[i+6:])
                version += new_version
                i += new_length
            return version, i
        else:
            num_of_subpackets = int(binary_rep[7:18])

print(get_packet_info("D2FE28"))
