from collections import defaultdict
from itertools import product
from typing import Dict, Literal, Tuple

test_input = (4, 8)
full_input = (7, 2)


# Shared
def f(n: int) -> int:
    return ((n - 1) % 10) + 1


# Part 1
def get_score_turns_product(p1_start: int, p2_start: int) -> int:
    num_dice_throws = 0
    positions = [p1_start, p2_start]
    scores = [0, 0]
    curr_player = 0
    while True:
        num_dice_throws += 3
        positions[curr_player] = f(positions[curr_player] + 3*(num_dice_throws-1))
        scores[curr_player] += positions[curr_player]
        if scores[curr_player] >= 1000:
            return num_dice_throws * scores[1-curr_player]
        curr_player = 1 - curr_player

assert get_score_turns_product(*test_input) == 739785
print(get_score_turns_product(*full_input))


# Part 2 (dynamic programming wooo)
def get_winning_number_of_universe(p1_start: int, p2_start: int) -> int:
    start_position_and_score: Dict[Tuple[Tuple[int, int], Tuple[int, int], Literal[0, 1]], int] = {
        ((p1_start, 0), (p2_start, 0), 0): 1,
    }
    positions_and_scores = defaultdict(int, start_position_and_score)
    possible_moves = tuple(sum(x) for x in product(*([(1, 2, 3)] * 3)))
    max_score = 21 + max(possible_moves)

    for p1_score, p2_score in product(range(1, max_score + 1), range(max_score + 1)):
        for p1_pos, p2_pos in product(range(1, 11), range(1, 11)):
            positions_and_scores[((p1_pos, p1_score), (p2_pos, p2_score), 1)] = sum([
                positions_and_scores[((f(p1_pos-x), p1_score-p1_pos), (p2_pos, p2_score), 0)]
                for x in possible_moves if p1_score-p1_pos < 21 and p2_score < 21
            ])
            positions_and_scores[((p1_pos, p1_score), (p2_pos, p2_score), 0)] = sum([
                positions_and_scores[((p1_pos, p1_score), (f(p2_pos-x), p2_score-p2_pos), 1)]
                for x in possible_moves if p2_score-p2_pos < 21 and p1_score < 21
            ])

    p1_wins = sum([v for k,v in positions_and_scores.items() if k[0][1]>=21])
    p2_wins = sum([v for k,v in positions_and_scores.items() if k[1][1]>=21])
    return max(p1_wins, p2_wins)

assert get_winning_number_of_universe(*test_input) == 444356092776315
print(get_winning_number_of_universe(*full_input))
