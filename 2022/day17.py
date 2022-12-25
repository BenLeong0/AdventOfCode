from dataclasses import dataclass
from typing import Dict, List, NewType, Set, Tuple


# INPUT_FILE = "inputs/day17test.in"
INPUT_FILE = "inputs/day17.in"

WIND_DIRECTIONS = open(INPUT_FILE).read()
BLOCK_TYPES = [
    # first element is leftmost, last element is rightmost
    [(2,4),(3,4),(4,4),(5,4)],
    [(2,5),(3,4),(3,5),(3,6),(4,5)],
    [(2,4),(3,4),(4,4),(4,5),(4,6)],
    [(2,4),(2,5),(2,6),(2,7)],
    [(2,4),(3,4),(2,5),(3,5)],
]
WIND_INDEX = 0


@dataclass
class RockRecord:
    rock_index: int
    height: int

Coord = NewType("Coord", Tuple[int, int])
Block = NewType("Block", List[Coord])
Board = NewType("Board", Set[Coord])


def adjust_board(board: Board):
    height_above_zero = max(x[1] for x in board)
    adjusted_board: Board = {(b[0],b[1]-height_above_zero) for b in board}
    return adjusted_board


def get_height(board: Board) -> int:
    return - min(b[1] for b in board)


def main(num_rocks: int = 2022):
    board: Board = {(i,0) for i in range(7)}
    seen: Dict[Coord, RockRecord] = {}
    loops: Dict[Coord, RockRecord] = {}

    wind_idx = 0
    for curr_rock_idx in range(num_rocks + 1):
        board = adjust_board(board)

        block_type = curr_rock_idx % 5
        height = get_height(board)

        key = (block_type, wind_idx)
        if key in loops:
            preloop_idx = seen[key].rock_index
            preloop_height = seen[key].height

            first_loop_idx = loops[key].rock_index
            first_loop_height = loops[key].height

            if (height - preloop_height) % (first_loop_height - preloop_height) == 0:
                loop_height = first_loop_height - preloop_height
                num_rocks_in_loop = first_loop_idx - preloop_idx
                num_loops = (num_rocks - preloop_idx) // num_rocks_in_loop
                total_looping_height = loop_height * num_loops

                num_postloop_rocks = (num_rocks - preloop_idx) % num_rocks_in_loop
                non_loop_height = [
                    v.height for v in seen.values()
                    if v.rock_index == num_postloop_rocks + preloop_idx
                ][0]

                return non_loop_height + total_looping_height

        elif key in seen:
            loops[key] = RockRecord(curr_rock_idx, height)
        else:
            seen[key] = RockRecord(curr_rock_idx, height)

        curr_block = BLOCK_TYPES[block_type]
        while True:
            wind_dir = WIND_DIRECTIONS[wind_idx]
            wind_idx = (wind_idx + 1) % len(WIND_DIRECTIONS)

            if wind_dir == "<" and (
                curr_block[0][0] > 0 and
                not any((x[0]-1,x[1]) in board for x in curr_block)
            ):
                curr_block = [((x[0]-1,x[1]))for x in curr_block]

            if wind_dir == ">" and (
                curr_block[-1][0] < 6 and
                not any((x[0]+1,x[1]) in board for x in curr_block)
            ):
                curr_block = [((x[0]+1,x[1]))for x in curr_block]

            if any((x[0],x[1]-1) in board for x in curr_block):
                break

            curr_block = [(x[0],x[1]-1) for x in curr_block]

        board.update(curr_block)

    return get_height(board)


if __name__ == "__main__":
    part1 = main()
    part2 = main(1000000000000)

    print(part1)
    print(part2)
