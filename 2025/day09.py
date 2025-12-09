# ruff: noqa: E731


from itertools import combinations


INPUT_FILE_TEST = "inputs/day09.test.in"
INPUT_FILE = "inputs/day09.in"

part1ol = lambda filename: max((abs(int(a[0])-int(b[0]))+1)*(abs(int(a[1])-int(b[1]))+1) for a,b in combinations((list(map(int,x.split(","))) for x in open(filename).read().split("\n")[:-1]),2))

print(part1ol(INPUT_FILE_TEST))
print(part1ol(INPUT_FILE))
