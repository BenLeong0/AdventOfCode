test_dots = [
    (6, 10),
    (0, 14),
    (9, 10),
    (0, 3),
    (10 ,4),
    (4, 11),
    (6, 0),
    (6, 12),
    (4, 1),
    (0, 13),
    (10 ,12),
    (3, 4),
    (3, 0),
    (8, 4),
    (1, 10),
    (2, 14),
    (8, 10),
    (9, 0),
]

test_folds = [
    ("y", 7),
    ("x", 5),
]

with open("day13.in", "r", newline="\n") as readfile:
    file = readfile.read().replace('\r\n', '\n').split('\n\n')
    full_input = [[int(y) for y in x] for x in file[0].split('\n')]
    # full_boards = [
    #     [
    #         [int(x) for x in row.split()]
    #         for row in board.split('\n')
    #     ] for board in file[1:-1]
    # ]