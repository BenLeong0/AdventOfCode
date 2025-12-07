# ruff: noqa: E731

from functools import reduce
from utils import file_to_list

INPUT_FILE_TEST = "inputs/day01.test.in"
INPUT_FILE = "inputs/day01.in"


def part1(filename: str) -> int:
    rows = file_to_list(filename)

    curr = 50
    count = 0

    for row in rows:
        delta = int(row[1:])
        if row[0] == "L":
            delta *= -1

        curr = (curr + delta) % 100

        if curr == 0:
            count += 1

    return count


part1ol = lambda filename: reduce(lambda x,y:(x[0]+y,x[1]+int((x[0]+y)%100 == 0)),(((-1)**"LR".index(x[0]))*int(x[1:]) for x in open(filename).read().split("\n")[:-1]),(50,0))[1]

print(part1(INPUT_FILE_TEST))
print(part1ol(INPUT_FILE_TEST))
print(part1(INPUT_FILE))
print(part1ol(INPUT_FILE))


def part2(filename: str) -> int:
    rows = file_to_list(filename)

    curr = 50
    count = 0

    for row in rows:
        delta = int(row[1:])
        if row[0] == "L":
            delta *= -1

        prev, curr = curr, curr + delta
        count += abs((prev // 100) - (curr // 100))
        if row[0] == "L" and curr % 100 == 0:
            count += 1
        if row[0] == "L" and prev % 100 == 0:
            count -= 1

    return count


part2ol = lambda filename: reduce(lambda x,y:(x[0]+y,(x[1]+abs((x[0]//100)-((x[0]+y)//100))+int(y<0 and (x[0]+y)%100 == 0)-int(y<0 and (x[0])%100 == 0))),(((-1)**"LR".index(x[0]))*int(x[1:]) for x in open(filename).read().split("\n")[:-1]),(50,0))[1]

print(part2(INPUT_FILE_TEST))
print(part2ol(INPUT_FILE_TEST))
print(part2(INPUT_FILE))
print(part2ol(INPUT_FILE))
