# ruff: noqa: E731


from functools import reduce
from itertools import combinations
from math import sqrt


INPUT_FILE_TEST = "inputs/day08.test.in"
INPUT_FILE = "inputs/day08.in"

part1ol = lambda filename,num: reduce(lambda a,b:a*b,sorted(map(lambda s:len(s),reduce(lambda prev,n:[*[s for s in prev if n[0] not in s and n[1] not in s],{*sum([list(s) for s in prev if n[0] in s or n[1] in s],[]),*n}],map(lambda x:x[0],reduce(lambda prev,n:[*[x for x in prev if x[1]<n_tup[1]],n_tup,*[x for x in prev if x[1]>=n_tup[1]]][:num] if (n_tup := ((n[0],n[1]),sqrt((n[0][0]-n[1][0])**2+(n[0][1]-n[1][1])**2+(n[0][2]-n[1][2])**2))) else [],combinations((tuple(map(int,r.split(","))) for r in open(filename).read().split("\n")[:-1]),2),[])),[])),reverse=True)[:3])

print(part1ol(INPUT_FILE_TEST,10))
print(part1ol(INPUT_FILE,1000))
