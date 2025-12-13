# ruff: noqa: E731


INPUT_FILE_TEST = "inputs/day11.test.in"
INPUT_FILE = "inputs/day11.in"

part1ol = lambda filename: [e:={i:o.split(" ") for [i,o] in [x.split(": ") for x in open(filename).read().split("\n")[:-1]]},cache:={"out": 1},f:=lambda x="you":cache[x] if x in cache else sum(f(y) for y in e[x])][-1]()

print(part1ol(INPUT_FILE_TEST))
print(part1ol(INPUT_FILE))
