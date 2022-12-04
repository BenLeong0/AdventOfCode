import re

# INPUT_FILE = "inputs/day04test.in"
INPUT_FILE = "inputs/day04.in"

part1 = sum(a<=c<=d<=b or c<=a<=b<=d for a,b,c,d in [map(int,re.split(r"[,-]", r)) for r in open(INPUT_FILE).read().split("\n")])
part2 = sum(not(a>d or b<c)for a,b,c,d in [map(int,re.split(r"[,-]", r)) for r in open(INPUT_FILE).read().split("\n")])

print(part1)
print(part2)
