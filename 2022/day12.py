from itertools import takewhile
from string import ascii_lowercase

# INPUT_FILE = "inputs/day12test.in"
INPUT_FILE = "inputs/day12.in"

part1 = [list(list(takewhile(lambda _:(c.append(({(x+i,y+j)for x,y in c[-1][0] for i in[1,0,-1]for j in[1,0,-1]if abs(i+j)==1 and 0<=x+i<len(m)and 0<=y+j<len(m[0])and(x+i,y+j)not in c[-1][0].union(c[-1][1]) and abs(h[m[x+i][y+j]]-h[m[x][y]])<=1},c[-1][0].union(c[-1][1]),c[-1][2]+1)) or t not in c[-1][0]),c)for c in [[({(i,j)for i in range(len(m))for j in range(len(m[0]))if m[i][j]=="S"},{(i,j)for i in range(len(m))for j in range(len(m[0]))if m[i][j]=="S"},2)]]for t in [[(i,j)for i in range(len(m))for j in range(len(m[0]))if m[i][j]=="E"][0]])[0])[-1][2]for h in[{**{c:i for i,c in enumerate(ascii_lowercase)},"S":0,"E":25}]for m in[[list(r)for r in open(INPUT_FILE).read().split("\n")]]][0]
part2 = [list(list(takewhile(lambda _:(c.append(({(x+i,y+j)for x,y in c[-1][0] for i in[1,0,-1]for j in[1,0,-1]if abs(i+j)==1 and 0<=x+i<len(m)and 0<=y+j<len(m[0])and(x+i,y+j)not in c[-1][0].union(c[-1][1]) and abs(h[m[x+i][y+j]]-h[m[x][y]])<=1},c[-1][0].union(c[-1][1]),c[-1][2]+1)) or t not in c[-1][0]),c)for c in [[({(i,j)for i in range(len(m))for j in range(len(m[0]))if m[i][j]in"aS"},{(i,j)for i in range(len(m))for j in range(len(m[0]))if m[i][j]in"aS"},2)]]for t in [[(i,j)for i in range(len(m))for j in range(len(m[0]))if m[i][j]=="E"][0]])[0])[-1][2]for h in[{**{c:i for i,c in enumerate(ascii_lowercase)},"S":0,"E":25}]for m in[[list(r)for r in open(INPUT_FILE).read().split("\n")]]][0]

print(part1)
print(part2)
