# ruff: noqa: E731


from functools import reduce
from itertools import chain, combinations
from math import inf


INPUT_FILE_TEST = "inputs/day10.test.in"
INPUT_FILE = "inputs/day10.in"

part1ol = lambda filename: sum(min(len(presses) for presses in map(lambda p:[eval(b.replace(")",",)")) for b in p],chain.from_iterable(combinations(buttons,r) for r in range(len(buttons)+1))) if all(x==0 for x in reduce(lambda p,b:[1-c if any(x==i for x in b) else c for (i,c) in enumerate(p)],presses,[0 if c=="." else 1 for c in target[1:-1]]))) for [target,*buttons,_] in [x.split() for x in open(filename).read().split("\n")[:-1]])

print(part1ol(INPUT_FILE_TEST))
print(part1ol(INPUT_FILE))

part2ol = lambda filename:reduce(lambda a,b:a+b[-1](),([tj:=[int(x) for x in joltage[1:-1].split(",")],all_buttons:=sorted(set(eval(b.replace(")",",)"))) for b in buttons),cache:={tuple(0 for _ in tj):0},f:=(lambda pj=None:[pj1:={nj:len(button_comb) for button_comb in sorted(chain.from_iterable(combinations(all_buttons,r) for r in range(len(all_buttons)+1)),key=lambda x:-len(x)) if (nj:=tuple(reduce(lambda p,b:[c - 1 if any(x==i for x in b) else c for (i,c) in enumerate(p)],button_comb,pj or tj))) and all(j%2==0 for j in nj) and all(j >= 0 for j in nj)},min(((nj not in cache and cache.update({nj:(2*f([x//2 for x in nj]))})) or cache[nj]+n for nj,n in pj1.items()),default=inf)][-1])] for [_,*buttons,joltage] in [x.split() for x in open(filename).read().split("\n")[:-1]]),0)

print(part2ol(INPUT_FILE_TEST))
print(part2ol(INPUT_FILE))
