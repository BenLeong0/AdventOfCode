import copy
from typing import List


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
    arr = [int(x) for x in readfile.readline()[:-1].split(',')]
    boards = []
    curr_line = readfile.readline()
    curr_board = []
    while curr_line:
        if curr_line == '\n':
            boards.append(curr_board)
            curr_board = []
        else:
            curr_board.append([int(x) for x in curr_line[:-1].split()])
        curr_line = readfile.readline()
    boards = boards[1:]
    


# Shared
Board = List[List[int]]


def completed_board(board: Board, index: int) -> bool:
    # Rows
    if all([x == -1 for x in board[index//5]]):
        return True

    # Columns
    if all([row[index%5] == -1 for row in board]):
        return True
    
    return False


def get_board_score(board: Board, final_num: int) -> int:
    total_score = 0
    for i in range(25):
        curr_score = board[i//5][i%5]
        if curr_score != -1:
            total_score += curr_score
    return total_score * final_num


# Part 1
def find_score_of_best_board(boards: List[Board], inputs: List[int]) -> int:
    for num in inputs:
        for board in boards:
            for i in range(25):
                if board[i//5][i%5] == num:
                    board[i//5][i%5] = -1
                    break
            if completed_board(board, i):
                return get_board_score(board, num)



assert find_score_of_best_board(copy.deepcopy(test_boards), test_input) == 4512
print(find_score_of_best_board(copy.deepcopy(boards), arr))


# Part 2
def find_score_of_worst_board(boards: List[Board], inputs: List[int]) -> int:
    for num in inputs:
        board_num = 0
        while board_num < len(boards):
            board = boards[board_num]
            for i in range(25):
                if board[i//5][i%5] == num:
                    board[i//5][i%5] = -1
                    break
            if completed_board(board, i):
                if len(boards) == 1:
                    return get_board_score(board, num)
                else:
                    del boards[board_num]
            else:
                board_num += 1



assert find_score_of_worst_board(copy.deepcopy(test_boards), test_input) == 1924
print(find_score_of_worst_board(copy.deepcopy(boards), arr))