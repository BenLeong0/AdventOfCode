# ruff: noqa: E731


INPUT_FILE = "inputs/day12.in"

part1ol = lambda filename: len([x for x,y in [(eval(row.split(": ")[0].replace("x",",")),[int(x) for x in row.split(": ")[1].split()]) for row in open(filename).read()[:-1].split("\n\n")[-1].split("\n")] if x[0]*x[1]>=9*sum(y)])

print(part1ol(INPUT_FILE))
