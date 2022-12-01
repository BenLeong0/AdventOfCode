from itertools import combinations

print(max(sum(map(int, x.split("\n"))) for x in open("input/day01.in").read().split("\n\n")))
print(max(sum(y) for y in combinations([sum(map(int, x.split("\n"))) for x in open("input/day01.in").read().split("\n\n")], r=3)))
