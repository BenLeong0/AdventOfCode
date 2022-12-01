from itertools import combinations


INPUT_FILE = "input/day01.in"

print(max(sum(map(int, x.split("\n"))) for x in open(INPUT_FILE).read().split("\n\n")))
print(max(sum(y) for y in combinations([sum(map(int, x.split("\n"))) for x in open(INPUT_FILE).read().split("\n\n")], r=3)))
