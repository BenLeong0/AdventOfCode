# INPUT_FILE = "inputs/day06test1.in"
# INPUT_FILE = "inputs/day06test2.in"
# INPUT_FILE = "inputs/day06test3.in"
# INPUT_FILE = "inputs/day06test4.in"
# INPUT_FILE = "inputs/day06test5.in"
INPUT_FILE = "inputs/day06.in"

part1 = [[len(set(r[i-4:i]))==4 for i in range(4,len(r))].index(True)+4 for r in open(INPUT_FILE).read().split("\n")][0]
part2 = [[len(set(r[i-14:i]))==14 for i in range(14,len(r))].index(True)+14 for r in open(INPUT_FILE).read().split("\n")][0]

print(part1)
print(part2)
