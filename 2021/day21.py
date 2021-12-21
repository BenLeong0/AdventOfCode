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


# Part 2
# DYNAMIC PROGRAMMING!!
# f(s1, s2, p1, p2) = #universes where score = (s1, s2), and it's p1's turn
# g(s1, s2, p1, p2) = #universes where score = (s1, s2), and it's p2's turn
# f(s1, s2, p1, p2) = g(s1, s2-1) + g(s1, s2-2) + g(s1, s2-3)
def get_winning_number_of_universe(p1_start: int, p2_start: int) -> int:
    start_position_and_score: Dict[Tuple[Tuple[int,int],Tuple[int,int],Literal[0,1]],int] = {
        ((p1_start, 0), (p2_start, 0), 0): 1,
    }
    positions_and_scores = defaultdict(int, start_position_and_score)
    for p2_score, p1_score in product(range(23), range(1,23)):
        for p1_pos, p2_pos in product(range(1, 11), range(1, 11)):
            positions_and_scores[((p1_pos, p1_score), (p2_pos, p2_score), 1)] = sum([
                positions_and_scores[((f(p1_pos-x), p1_score-p1_pos), (p2_pos, p2_score), 0)]
                for x in range(1, 4) if p1_score-p1_pos < 21 and p2_score < 21
            ])
            positions_and_scores[((p1_pos, p1_score), (p2_pos, p2_score), 0)] = sum([
                positions_and_scores[((p1_pos, p1_score), (f(p2_pos-x), p2_score-p2_pos), 1)]
                for x in range(1, 4) if p2_score-p2_pos < 21 and p1_score < 21
            ])

    p1_wins = sum([v for k,v in positions_and_scores.items() if k[0][1]>=21])
    return p1_wins

# Back tracking?
def get_winning_number_of_universes_recursive(p1_start: int, p2_start: int) -> int:
    wins = [0, 0]
    pos_and_sco = [{"pos": p1_start, "score": 0}, {"pos": p2_start, "score": 0}]

    def play_turn(curr_player=0):
        print(pos_and_sco)
        for roll in (1,2,3):
            pos_and_sco[curr_player]['pos'] = f(pos_and_sco[curr_player]['pos']+roll)
            pos_and_sco[curr_player]['score'] += pos_and_sco[curr_player]['pos']
            if pos_and_sco[curr_player]['score'] < 21:
                play_turn(curr_player=1-curr_player)
            else:
                wins[curr_player] += 1
            pos_and_sco[curr_player]['score'] -= pos_and_sco[curr_player]['pos']
            pos_and_sco[curr_player]['pos'] = f(pos_and_sco[curr_player]['pos']-roll)

    play_turn()

    return max(wins)

print(get_winning_number_of_universes_recursive(*test_input))
