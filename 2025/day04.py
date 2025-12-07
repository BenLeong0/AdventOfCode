# ruff: noqa: E731

from functools import reduce
from itertools import product


INPUT_FILE_TEST = "inputs/day04.test.in"
INPUT_FILE = "inputs/day04.in"


part1ol = lambda filename: len([(rows:=open(filename).read().split("\n")[:-1]),(w:=len(rows[0])),(h:=len(rows)),(n:=lambda i,j:(rows[i][j]!="@" or len([(x,y) for (x,y) in product(range(i-1,i+2),range(j-1,j+2)) if (x!=i or y!=j) and 0<=x<w and 0<=y<h and rows[x][y] == "@"]))),[0 for (x,y) in product(range(w),range(h)) if rows[x][y] == "@" and n(x,y)<4]][4])


print(part1ol(INPUT_FILE_TEST))
print(part1ol(INPUT_FILE))

part2ol = lambda filename: [(rows:=open(filename).read().split("\n")[:-1]),(w:=len(rows[0])),(h:=len(rows)),(rd:={(x,y): rows[x][y] == "@" for (x,y) in product(range(w),range(h))}),(n:=lambda i,j,r:(not r[i,j] or len([(x,y) for (x,y) in product(range(i-1,i+2),range(j-1,j+2)) if (x!=i or y!=j) and 0<=x<w and 0<=y<h and r[x,y]]))),(sum(rd.values())-sum(reduce(lambda prev,next:{(x,y): v and n(x,y,prev)>=4 for ((x,y),v) in prev.items()},range(100),rd).values()))][5]


print(part2ol(INPUT_FILE_TEST))
print(part2ol(INPUT_FILE))
