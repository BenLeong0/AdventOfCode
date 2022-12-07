from functools import reduce
from re import search, sub

# INPUT_FILE = "inputs/day07test.in"
INPUT_FILE = "inputs/day07.in"

part1 = [sum(v for v in {d:sum(v for k,v in m.items()if search("^"+d,k))for d in m}.values()if v<=100000)for m in[reduce(lambda c,n: ([(sub("[^/]+/$","",c[0])if n[2]==".."else f"{c[0]}{n[2]}/"),0,c[2]]if n[1]=="cd"else[c[0],c[1],{**c[2],c[0]:c[1]}]if n[0]=="dir"or n[1]=="ls"else[c[0],c[1]+int(n[0]),{**c[2],c[0]:c[1]+int(n[0])}]),[r.split(" ")for r in open(INPUT_FILE).read().split("\n")[1:]],["/",0,{}])[2]]][0]
part2 = [[min(v for v in t.values()if v>=t['/']-40000000)for t in[{d:sum(v for k,v in m.items()if search("^"+d,k))for d in m}]][0]for m in[reduce(lambda c,n: ([(sub("[^/]+/$","",c[0])if n[2]==".."else f"{c[0]}{n[2]}/"),0,c[2]]if n[1]=="cd"else[c[0],c[1],{**c[2],c[0]:c[1]}]if n[0]=="dir"or n[1]=="ls"else[c[0],c[1]+int(n[0]),{**c[2],c[0]:c[1]+int(n[0])}]),[r.split(" ")for r in open(INPUT_FILE).read().split("\n")[1:]],["/",0,{}])[2]]][0]

print(part1)
print(part2)
