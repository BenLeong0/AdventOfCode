from functools import cmp_to_key
from json import loads

# INPUT_FILE = "inputs/day13test.in"
INPUT_FILE = "inputs/day13.in"

part1 = sum(i+1 for(i,p)in enumerate((loads(r.split("\n")[0]),loads(r.split("\n")[1])) for r in open(INPUT_FILE).read().split("\n\n")) if (lambda a:lambda v,u:a(a,v,u))(lambda s,x,y:(0 if x==y else (-1 if x<y else 1) if type(x)==type(y)==int else s(s,x,[y])if type(y)==int else s(s,[x],y)if type(x)==int else [s(s,a,b) for a,b in zip(x,y) if a!=b][0]if len(x)==len(y)else (-1 if x==y[:len(x)] else [s(s,a,b) for a,b in zip(x,y[:len(x)])if a!=b][0])if len(x)<len(y)else (1 if x[:len(y)]==y else [s(s,a,b) for a,b in zip(x[:len(y)],y)if a!=b][0])))(*p)==-1)
part2 = [y.index([2])*y.index([6])for y in [sorted([[],[2],[6]]+[loads(r)for r in open(INPUT_FILE).read().replace("\n\n","\n").split("\n")],key=cmp_to_key((lambda a:lambda v,u:a(a,v,u))(lambda s,x,y:(0 if x==y else (-1 if x<y else 1) if type(x)==type(y)==int else s(s,x,[y])if type(y)==int else s(s,[x],y)if type(x)==int else [s(s,a,b) for a,b in zip(x,y) if a!=b][0]if len(x)==len(y)else (-1 if x==y[:len(x)] else [s(s,a,b) for a,b in zip(x,y[:len(x)])if a!=b][0])if len(x)<len(y)else (1 if x[:len(y)]==y else [s(s,a,b) for a,b in zip(x[:len(y)],y)if a!=b][0])))))]][0]

print(part1)
print(part2)
