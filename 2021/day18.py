import copy
from typing import Iterable, List, Optional, Tuple, Union

SnailfishNumber = List[Union[int, Iterable['SnailfishNumber']]]

test_input: List[SnailfishNumber] = [
    [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]],
    [[[5,[2,8]],4],[5,[[9,9],0]]],
    [6,[[[6,2],[5,6]],[[7,6],[4,7]]]],
    [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]],
    [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]],
    [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]],
    [[[[5,4],[7,7]],8],[[8,3],8]],
    [[9,3],[[9,9],[6,[4,9]]]],
    [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]],
    [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]],
]

with open("inputs/day18.in", "r", newline="\n") as readfile:
    full_input = [eval(line[:-1]) for line in readfile.readlines()]


# Shared
def add_to_left_side(inpt: list, value: int) -> None:
    if type(inpt[0]) == int:
        inpt[0] += value
    else:
        add_to_left_side(inpt[0], value)

def add_to_right_side(inpt: list, value: int) -> None:
    if type(inpt[1]) == int:
        inpt[1] += value
    else:
        add_to_right_side(inpt[1], value)

def explode(inpt: list, depth: int = 0) -> Tuple[Optional[int], Optional[int], bool]:
    # Left node
    if type(inpt[0]) == list:
        if depth == 3:
            l, r = inpt[0]
            inpt[0] = 0
            if type(inpt[1]) == int:
                inpt[1] += r
            else:
                add_to_left_side(inpt[1], r)
            return l, None, True
        l, r, reduced = explode(inpt[0], depth+1)

        if r is not None:
            if type(inpt[1]) == int:
                inpt[1] += r
            else:
                add_to_left_side(inpt[1], r)
            return l, None, True

        if reduced:
            return l, None, True

    # Right node
    if type(inpt[1]) == list:
        if depth == 3:
            l, r = inpt[1]
            inpt[1] = 0
            if type(inpt[0]) == int:
                inpt[0] += l
            else:
                add_to_left_side(inpt[1], l)
            return None, r, True

        l, r, reduced = explode(inpt[1], depth+1)

        if l is not None:
            if type(inpt[0]) == int:
                inpt[0] += l
            else:
                add_to_right_side(inpt[0], l)
            return None, r, True

        if reduced:
            return None, r, True

    return None, None, False

def split(inpt: list) -> bool:
    # Left node
    if type(inpt[0]) == int and inpt[0] >= 10:
        inpt[0] = [inpt[0]//2, (inpt[0]+1)//2]
        return True
    elif type(inpt[0]) == list:
        splitted = split(inpt[0])
        if splitted:
            return True

    # Right node
    if type(inpt[1]) == int and inpt[1] >= 10:
        inpt[1] = [inpt[1]//2, (inpt[1]+1)//2]
        return True
    elif type(inpt[1]) == list:
        splitted = split(inpt[1])
        if splitted:
            return True

    return False


def fully_reduce(inpt: list) -> None:
    still_reducing = True
    while still_reducing:
        _, __, exploded = explode(inpt)
        if not exploded:
            splitted = split(inpt)
        still_reducing = exploded or splitted

    return inpt

x = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
assert fully_reduce([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]) == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]


# Part 1
def get_final_sum(snailfish_numbers: list) -> int:
    curr_num = snailfish_numbers[0]
    for number in snailfish_numbers[1:]:
        curr_num = fully_reduce([curr_num, number])
    return curr_num

assert get_final_sum([[1,1],[2,2],[3,3],[4,4]]) == [[[[1,1],[2,2]],[3,3]],[4,4]]
assert get_final_sum([[1,1],[2,2],[3,3],[4,4],[5,5]]) == [[[[3,0],[5,3]],[4,4]],[5,5]]
assert get_final_sum([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]) == [[[[5,0],[7,4]],[5,5]],[6,6]]
assert get_final_sum([
    [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],
    [7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
    [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
    [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],
    [7,[5,[[3,8],[1,4]]]],
    [[2,[2,2]],[8,[8,1]]],
    [2,9],
    [1,[[[9,3],9],[[9,0],[0,7]]]],
    [[[5,[7,4]],7],1],
    [[[[4,2],2],6],[8,7]],
]) == [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
assert get_final_sum(copy.deepcopy(test_input)) == [[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]


def get_magnitude(snailfish_numbers: Union[list, int]) -> int:
    if type(snailfish_numbers) == int:
        return snailfish_numbers
    return 3*get_magnitude(snailfish_numbers[0]) + 2*get_magnitude(snailfish_numbers[1])


def get_magnitude_of_final_sum(snailfish_numbers: list) -> int:
    final_sum = get_final_sum(snailfish_numbers)
    return get_magnitude(final_sum)

assert get_magnitude_of_final_sum(copy.deepcopy(test_input)) == 4140
print(get_magnitude_of_final_sum(copy.deepcopy(full_input)))


# Part 2
def get_max_magnitude(snailfish_numbers: list) -> int:
    curr_max = 0
    for i in range(len(snailfish_numbers)):
        for j in range(len(snailfish_numbers)):
            if i == j:
                continue
            curr_max = max(
                curr_max,
                get_magnitude_of_final_sum([
                    copy.deepcopy(snailfish_numbers[i]),
                    copy.deepcopy(snailfish_numbers[j])
                ])
            )
    return curr_max

assert get_max_magnitude(copy.deepcopy(test_input)) == 3993
print(get_max_magnitude(full_input))
