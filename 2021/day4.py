import copy
from typing import List, Tuple


test_boards = [
    [
        [ 22, 13, 17, 11,  0 ],
        [  8,  2, 23,  4, 24 ],
        [ 21,  9, 14, 16,  7 ],
        [  6, 10,  3, 18,  5 ],
        [  1, 12, 20, 15, 19 ],
    ],
    [
        [  3, 15,  0,  2, 22 ],
        [ 9 , 18, 13, 17,  5 ],
        [ 19,  8,  7, 25, 23 ],
        [ 20, 11, 10, 24,  4 ],
        [ 14, 21, 16, 12,  6 ],
    ],
    [
        [ 14, 21, 17, 24,  4 ],
        [ 10, 16, 15,  9, 19 ],
        [ 18,  8, 23, 26, 20 ],
        [ 22, 11, 13,  6,  5 ],
        [  2,  0, 12,  3,  7 ],
    ]
]

test_input = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

with open("day4.in", "r", newline="\n") as readfile:
    full_input = [int(x) for x in readfile.readline()[:-1].split(',')]
    full_boards = []
    curr_board = []
    for line in readfile.readlines()[1:]:
        if line == '\n':
            full_boards.append(curr_board)
            curr_board = []
        else:
            curr_board.append([int(x) for x in line[:-1].split()])
    full_boards = full_boards



# Shared
Board = List[List[int]]

# i//5 == j//5  =>  i and j are in the same row
# i%5 == j%5  =>  i and j are in the same column

def completed_board(board: Board, index: int) -> bool:
    return (
        all([x == -1 for x in board[index//5]]) or      # Rows
        all([row[index%5] == -1 for row in board])      # Columns
    )


def get_board_score(board: Board, final_num: int) -> int:
    total_score = 0
    for i in range(25):
        curr_score = board[i//5][i%5]
        if curr_score != -1:
            total_score += curr_score
    return total_score * final_num


# Part 1
def find_score_of_best_board(boards: List[Board], inputs: List[int]) -> int:
    boards = copy.deepcopy(boards)
    for num in inputs:
        for board in boards:
            for i in range(25):
                if board[i//5][i%5] == num:
                    board[i//5][i%5] = -1
                    break
            if completed_board(board, i):
                return get_board_score(board, num)

assert find_score_of_best_board(test_boards, test_input) == 4512
print(find_score_of_best_board(full_boards, full_input))


# Part 2
def find_score_of_worst_board(boards: List[Board], inputs: List[int]) -> int:
    boards = copy.deepcopy(boards)

    def get_board_age_and_score(board: Board, inputs: List[int]) -> Tuple[int, int]:
        for (age, num) in enumerate(inputs):
            for i in range(25):
                if board[i//5][i%5] == num:
                    board[i//5][i%5] = -1
                    break
            if completed_board(board, i):
                return age, get_board_score(board, num)

    return max([get_board_age_and_score(board, inputs) for board in boards], key=lambda x: x[0])[1]

assert find_score_of_worst_board(test_boards, test_input) == 1924
print(find_score_of_worst_board(full_boards, full_input))
