from typing import Tuple


test_input: str = "D2FE28"

with open("inputs/day16.in", "r", newline="\n") as readfile:
    full_input = readfile.read().splitlines()[0]


# Part 1
def get_version_sum(hex_input: str) -> int:
    binary_rep = bin(int(hex_input, 16))[2:].zfill(4*len(hex_input))

    def get_packet_info(start_idx: int = 0) -> Tuple[int,int]:
        """Return tuple of form `(version sum, packet length)`"""
        if "1" not in binary_rep[start_idx:]:
            return 0, len(binary_rep)

        version = int(binary_rep[start_idx+0:start_idx+3], 2)
        type_id = int(binary_rep[start_idx+3:start_idx+6], 2)

        if type_id == 4:
            curr_num = ''
            curr_idx = start_idx + 6
            while '1' in binary_rep[curr_idx:]:
                curr_packet = binary_rep[curr_idx:curr_idx+5]
                curr_num += curr_packet[1:]
                curr_idx += 5
                if curr_packet[0] == '0':
                    break
            return version, curr_idx

        length_type_id = binary_rep[start_idx+6]
        if length_type_id == '0':
            length = int(binary_rep[start_idx+7:start_idx+22], 2)
            curr_idx = start_idx + 22
            while (curr_idx < start_idx + length + 22) and ('1' in binary_rep[curr_idx:]):
                new_version, curr_idx = get_packet_info(curr_idx)
                version += new_version
            return version, curr_idx

        else:
            num_of_subpackets = int(binary_rep[start_idx+7:start_idx+18], 2)
            curr_idx = start_idx + 18
            for _ in range(num_of_subpackets):
                new_version, curr_idx = get_packet_info(curr_idx)
                version += new_version
            return version, curr_idx

    return get_packet_info()[0]

assert get_version_sum("D2FE28") == 6
assert get_version_sum("8A004A801A8002F478") == 16
assert get_version_sum("620080001611562C8802118E34") == 12
assert get_version_sum("C0015000016115A2E0802F182340") == 23
assert get_version_sum("A0016C880162017C3686B18A3D4780") == 31
print(get_version_sum(full_input))


# Part 2
def evaluate_with_operations(hex_input: str) -> int:
    binary_rep = bin(int(hex_input, 16))[2:].zfill(4*len(hex_input))

    operations = {
        0: lambda x,y: x+y if x is not None else y,
        1: lambda x,y: x*y if x is not None else y,
        2: lambda x,y: min(x,y) if x is not None else y,
        3: lambda x,y: max(x,y) if x is not None else y,
        5: lambda x,y: (1 if y < x else 0) if x is not None else y,
        6: lambda x,y: (1 if y > x else 0) if x is not None else y,
        7: lambda x,y: (1 if y == x else 0) if x is not None else y,
    }

    def get_packet_info(start_idx: int = 0) -> Tuple[int,int,int]:
        """Return tuple of form `(end_idx, value)`"""
        if "1" not in binary_rep[start_idx:]:
            return 0, len(binary_rep)

        type_id = int(binary_rep[start_idx+3:start_idx+6], 2)

        if type_id == 4:
            curr_value_bin = ''
            curr_idx = start_idx + 6
            while '1' in binary_rep[curr_idx:]:
                curr_packet = binary_rep[curr_idx:curr_idx+5]
                curr_value_bin += curr_packet[1:]
                curr_idx += 5
                if curr_packet[0] == '0':
                    break
            return curr_idx, int(curr_value_bin, 2)

        length_type_id = binary_rep[start_idx+6]
        operation = operations[type_id]
        curr_value = None

        idx_past_header = start_idx + 7

        if length_type_id == '0':
            length = int(binary_rep[idx_past_header:idx_past_header+15], 2)
            curr_idx = idx_past_header + 15
            while (curr_idx < idx_past_header + length + 15) and ('1' in binary_rep[curr_idx:]):
                curr_idx, new_value = get_packet_info(curr_idx)
                curr_value = operation(curr_value, new_value)
            return curr_idx, curr_value

        if length_type_id == '1':
            num_of_subpackets = int(binary_rep[idx_past_header:idx_past_header+11], 2)
            curr_idx = idx_past_header + 11
            for _ in range(num_of_subpackets):
                curr_idx, new_value = get_packet_info(curr_idx)
                curr_value = operation(curr_value, new_value)
            return curr_idx, curr_value

    return get_packet_info()[1]

assert evaluate_with_operations("C200B40A82") == 3
assert evaluate_with_operations("04005AC33890") == 54
assert evaluate_with_operations("880086C3E88112") == 7
assert evaluate_with_operations("CE00C43D881120") == 9
assert evaluate_with_operations("D8005AC2A8F0") == 1
assert evaluate_with_operations("F600BC2D8F") == 0
assert evaluate_with_operations("9C005AC2F8F0") == 0
assert evaluate_with_operations("9C0141080250320F1802104A08") == 1
print(evaluate_with_operations(full_input))
