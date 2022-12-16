from functools import reduce
from re import search

# INPUT_FILE, ROW_TO_CHECK, RANGE = "inputs/day15test.in", 10, 20
INPUT_FILE, ROW_TO_CHECK, RANGE = "inputs/day15.in", 2_000_000, 4_000_000

part1 = len([reduce(lambda s,c:s.union(set(range(-(abs(c[0]-c[2])+abs(c[1]-c[3])-abs(c[1]-ROW_TO_CHECK))+c[0],(abs(c[0]-c[2])+abs(c[1]-c[3])-abs(c[1]-ROW_TO_CHECK))+1+c[0]))),f,set())-{c[2]for c in f if c[3]==ROW_TO_CHECK}for f in[[list(map(int,search(r"[^-\d]+(-?\d+)"*4,r).groups()))for r in open(INPUT_FILE).read().split("\n")]]][0])
part2 = [[4000000*m+n for m,n in sum([sum([[(x,y) for x,y in [(a+i,b+l+1-i),(a-i,b+l+1-i),(a+l+1-i,b-i),(a+i-l-1,b-i)]if 0<=x<=RANGE and 0<=y<=RANGE and all(abs(x-c)+abs(y-d)>r for(c,d,r)in s)]for i in range(l+2)],[])for(a,b,l)in s],[])][0]for s in [[(c[0],c[1],abs(c[0]-c[2])+abs(c[1]-c[3]))for c in [list(map(int,search(r"[^-\d]+(-?\d+)"*4,r).groups()))for r in open(INPUT_FILE).read().split("\n")]]]][0]

print(part1)
print(part2)
