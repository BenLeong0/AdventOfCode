# ruff: noqa: E731


from itertools import combinations


INPUT_FILE_TEST = "inputs/day09.test.in"
INPUT_FILE = "inputs/day09.in"

part1ol = lambda filename: max((abs(int(a[0])-int(b[0]))+1)*(abs(int(a[1])-int(b[1]))+1) for a,b in combinations((list(map(int,x.split(","))) for x in open(filename).read().split("\n")[:-1]),2))

print(part1ol(INPUT_FILE_TEST))
print(part1ol(INPUT_FILE))

part2ol = lambda filename: [pairs:=[(a,b) for a,b in combinations((list(map(int,x.split(","))) for x in open(filename).read().split("\n")[:-1]),2) if a[0]==b[0] or a[1]==b[1]],max((abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1) for a,b in combinations((list(map(int,x.split(","))) for x in open(filename).read().split("\n")[:-1]),2) if all(min(a[0],b[0])>=max(x[0],y[0]) or max(a[0],b[0])<=min(x[0],y[0]) or min(a[1],b[1])>=max(x[1],y[1]) or max(a[1],b[1])<=min(x[1],y[1]) for x,y in pairs))][1]

print(part2ol(INPUT_FILE_TEST))
print(part2ol(INPUT_FILE))
