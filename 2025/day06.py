# ruff: noqa: E731

import re
from functools import reduce


INPUT_FILE_TEST = "inputs/day06.test.in"
INPUT_FILE = "inputs/day06.in"


part1ol = lambda filename: [(rows:=[re.split(r"\s+",x.strip()) for x in open(filename).read().split("\n")[:-1]]),sum(reduce({"+":lambda a,b:int(a)+int(b),"*":lambda a,b:int(a) * int(b)}[rows[-1][c]],[r[c] for r in rows[:-1]]) for c in range(len(rows[0])))][1]

print(part1ol(INPUT_FILE_TEST))
print(part1ol(INPUT_FILE))


part2ol = lambda filename: [(f:=open(filename).read().split("\n")[:-1]),(rows:=[r.rjust(len(f[0])+1) for r in f]),reduce(lambda p,n: (p[0]+p[1],0,"+") if all(row[n]==" " for row in rows) else (p[0],{"+":lambda a,b:a+int(b),"*":lambda a,b:(a or 1) * int(b)}[(o:=rows[-1][n] if rows[-1][n]!=" " else p[2])](p[1],int("".join(row[n] for row in rows[:-1]))),o),range(len(rows[0])),(0,0,"+"))][2][0]

print(part2ol(INPUT_FILE_TEST))
print(part2ol(INPUT_FILE))
