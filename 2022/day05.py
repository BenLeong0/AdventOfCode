from functools import reduce
from re import findall

# INPUT_FILE = "inputs/day05test.in"
INPUT_FILE = "inputs/day05.in"

part1 = "".join(next(zip([reduce(lambda n,t:{**n,t[1]:n[t[1]][t[0]:],t[2]:n[t[1]][:t[0]][::-1]+n[t[2]]},[list(map(int,findall("\d+",r)))for r in f[f.index("")+1:]],[{i:"".join(s).replace(" ","")for i,s in enumerate(list(zip(*f[:f.index("")-1]))[1::4],1)}][0])for f in[open(INPUT_FILE).read().split("\n")]][0].values())))
part2 = "".join(next(zip([reduce(lambda n,t:{**n,t[1]:n[t[1]][t[0]:],t[2]:n[t[1]][:t[0]]+n[t[2]]},[list(map(int,findall("\d+",r)))for r in f[f.index("")+1:]],[{i:"".join(s).replace(" ","")for i,s in enumerate(list(zip(*f[:f.index("")-1]))[1::4],1)}][0])for f in[open(INPUT_FILE).read().split("\n")]][0].values())))

print(part1)
print(part2)
