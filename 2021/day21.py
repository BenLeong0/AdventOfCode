from collections import defaultdict
from itertools import product
from typing import DefaultDict, List, Literal, Tuple

# Types
Position = int
Score = int
PlayerTurn = Literal[0, 1]
PlayerState = Tuple[Position, Score]
GameState = Tuple[PlayerState, PlayerState, PlayerTurn]

# Inputs
test_input: Tuple[Position, Position] = (4, 8)
full_input: Tuple[Position, Position] = (7, 2)

# Shared
def mod(n: Position) -> Position:
    return ((n - 1) % 10) + 1


# Part 1
def get_score_turns_product(p1_start: int, p2_start: int) -> int:
    num_dice_throws: int = 0
    positions: List[Position] = [p1_start, p2_start]
    scores: List[Score] = [0, 0]
    curr_player: PlayerTurn = 1
    while scores[curr_player] < 1000:
        curr_player = 1 - curr_player
        num_dice_throws += 3
        positions[curr_player] = mod(positions[curr_player] + 3*(num_dice_throws-1))
        scores[curr_player] += positions[curr_player]
    return num_dice_throws * scores[1-curr_player]

assert get_score_turns_product(*test_input) == 739785
print(get_score_turns_product(*full_input))


# Part 2 (dynamic programming wooo)
def get_winning_number_of_universe(p1_start: int, p2_start: int) -> int:
    positions_and_scores: DefaultDict[GameState, int] = defaultdict(int, {
        ((p1_start, 0), (p2_start, 0), 0): 1,
    })
    possible_moves = [sum(x) for x in product((1, 2, 3), repeat=3)]
    max_score = 21 + max(possible_moves)

    for p1_score, p2_score in product(range(1, max_score + 1), range(max_score + 1)):
        for p1_pos, p2_pos in product(range(1, 11), range(1, 11)):
            positions_and_scores[((p1_pos, p1_score), (p2_pos, p2_score), 1)] = sum([
                positions_and_scores[((mod(p1_pos-x), p1_score-p1_pos), (p2_pos, p2_score), 0)]
                for x in possible_moves if p1_score-p1_pos < 21 and p2_score < 21
            ])
            positions_and_scores[((p1_pos, p1_score), (p2_pos, p2_score), 0)] = sum([
                positions_and_scores[((p1_pos, p1_score), (mod(p2_pos-x), p2_score-p2_pos), 1)]
                for x in possible_moves if p2_score-p2_pos < 21 and p1_score < 21
            ])

    p1_wins = sum([v for k,v in positions_and_scores.items() if k[0][1]>=21])
    p2_wins = sum([v for k,v in positions_and_scores.items() if k[1][1]>=21])
    return max(p1_wins, p2_wins)

assert get_winning_number_of_universe(*test_input) == 444356092776315
print(get_winning_number_of_universe(*full_input))
