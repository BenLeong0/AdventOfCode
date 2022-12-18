from itertools import takewhile

# INPUT_FILE = "inputs/day18test.in"
INPUT_FILE = "inputs/day18.in"

part1 = [sum(6-sum(sum(m.get(abs(x[i]-y[i]),0)for i in range(3))==2+1j for y in f)for x in f)for m in[{0:1,1:1j}]for f in[[list(map(int,r.split(",")))for r in open(INPUT_FILE).read().split("\n")]]][0]
part2 = [[list(takewhile(lambda x:type(x)==dict or x!=None and(not any(q[-2].update({0:q[-2][0]+1})if n in f else v.add(n)or q.insert(-2,n)for n in [(x[0]+(i if j==0 else 0),x[1]+(i if j==1 else 0),x[2]+(i if j==2 else 0))for i in(-1,1)for j in (0,1,2)if(x[0]+(i if j==0 else 0),x[1]+(i if j==1 else 0),x[2]+(i if j==2 else 0))not in v and x[0]+(i if j==0 else 0)not in(-2, l[0]+2)and x[1]+(i if j==1 else 0)not in(-2, l[1]+2)and x[2]+(i if j==2 else 0)not in(-2, l[2]+2)])),q))for l in [[max(b[i] for b in f)for i in (0,1,2)]]][0]for q in [[(-1,-1,-1), {0:0}, None]]for f in [[tuple(map(int,r.split(",")))for r in open(INPUT_FILE).read().split("\n")]]for v in [set()]][0][-1][0]

print(part1)
print(part2)
