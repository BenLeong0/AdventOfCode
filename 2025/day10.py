# ruff: noqa: E731


from functools import reduce
from itertools import chain,combinations


INPUT_FILE_TEST = "inputs/day10.test.in"
INPUT_FILE = "inputs/day10.in"

part1ol = lambda filename: sum(min(len(presses) for presses in map(lambda p:[eval(b.replace(")",",\)")) for b in p],chain.from_iterable(combinations(buttons,r) for r in range(len(buttons)+1))) if all(x==0 for x in reduce(lambda p,b:[1-c if any(x==i for x in b) else c for (i,c) in enumerate(p)],presses,[0 if c=="." else 1 for c in target[1:-1]]))) for [target,*buttons,_] in [x.split() for x in open(filename).read().split("\n")[:-1]])

print(part1ol(INPUT_FILE_TEST))
print(part1ol(INPUT_FILE))
