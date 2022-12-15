from itertools import takewhile

# INPUT_FILE = "inputs/day14test.in"
INPUT_FILE = "inputs/day14.in"

part1 = [[len(list([takewhile(lambda _: (c.append((c[-1][0],(c[-1][1][0],c[-1][1][1]+1))if(c[-1][1][0],c[-1][1][1]+1)not in c[-1][0]else(c[-1][0],(c[-1][1][0]-1,c[-1][1][1]+1))if(c[-1][1][0]-1,c[-1][1][1]+1)not in c[-1][0]else(c[-1][0],(c[-1][1][0]+1,c[-1][1][1]+1))if(c[-1][1][0]+1,c[-1][1][1]+1)not in c[-1][0]else({*c[-1][0],c[-1][1]},(500,0)))or c[-2][1][1]!=l+1),c)for c in [[(p,(500,0))]]][0])[-1][0])-len(p)for p in[set(sum([sum([[(x,y)for x in range(min(r[i][0],r[i+1][0]),1+max(r[i][0],r[i+1][0]))for y in range(min(r[i][1],r[i+1][1]),1+max(r[i][1],r[i+1][1]))]for i in range(len(r)-1)],[])for r in f],[]))]for l in[max(max(x[1]for x in r)for r in f)]][0]for f in [[[list(map(int,l.split(",")))for l in r]for r in[l.split(" -> ") for l in open(INPUT_FILE).read().split("\n")]]]][0]
part2 = [[list([takewhile(lambda _: (c.append((c[-1][0],c[-1][1]+1)if (c[-1][0],c[-1][1]+1)not in p and c[-1][1]!=l+1 else(c[-1][0]-1,c[-1][1]+1)if (c[-1][0]-1,c[-1][1]+1)not in p and c[-1][1]!=l+1 else(c[-1][0]+1,c[-1][1]+1)if (c[-1][0]+1,c[-1][1]+1)not in p and c[-1][1]!=l+1 else(1 if p.add(c[-1])else(500,0)))or (500,0)not in p),c)for c in [[(500,0)]]][0])[-1][0]*0+len(p)-len(set(sum([sum([[(x,y)for x in range(min(r[i][0],r[i+1][0]),1+max(r[i][0],r[i+1][0]))for y in range(min(r[i][1],r[i+1][1]),1+max(r[i][1],r[i+1][1]))]for i in range(len(r)-1)],[])for r in f],[])))for p in[set(sum([sum([[(x,y)for x in range(min(r[i][0],r[i+1][0]),1+max(r[i][0],r[i+1][0]))for y in range(min(r[i][1],r[i+1][1]),1+max(r[i][1],r[i+1][1]))]for i in range(len(r)-1)],[])for r in f],[]))]for l in[max(max(x[1]for x in r)for r in f)]][0]for f in [[[list(map(int,l.split(",")))for l in r]for r in[l.split(" -> ") for l in open(INPUT_FILE).read().split("\n")]]]][0]

print(part1)
print(part2)
