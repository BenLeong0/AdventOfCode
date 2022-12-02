# INPUT_FILE = "input/day02test.in"
INPUT_FILE = "input/day02.in"

part1 = sum(((" XYZ".index(b)-"ABC".index(a))%3)*3+" XYZ".index(b) for a,_,b in open(INPUT_FILE).read().split("\n"))

print(part1)
