# INPUT_FILE = "input/day02test.in"
INPUT_FILE = "input/day02.in"

part1 = sum(((" XYZ".index(b)-"ABC".index(a))%3)*3+" XYZ".index(b) for a,_,b in open(INPUT_FILE).read().split("\n"))
part2 = sum(("XYZ".index(b)-1+"ABC".index(a))%3+1+"XYZ".index(b)*3 for a,_,b in open(INPUT_FILE).read().split("\n"))

print(part1)
print(part2)
