import re

# INPUT_FILE = "inputs/day04test.in"
INPUT_FILE = "inputs/day04.in"

part1 = sum(a<=c and b>=d or a>=c and b<=d for a,b,c,d in [map(int,re.split(r"[,-]", r)) for r in open(INPUT_FILE).read().split("\n")])
part2 = sum(a<=d and b>=c or a>=d and b<=c for a,b,c,d in [map(int,re.split(r"[,-]", r)) for r in open(INPUT_FILE).read().split("\n")])

print(part1)
print(part2)
