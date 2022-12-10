from functools import reduce
from re import sub

# INPUT_FILE = "inputs/day10test.in"
INPUT_FILE = "inputs/day10.in"

part1 = sum(reduce(lambda p,n:[*p,p[-1]+(int(n[1])if n[0]=="a" else 0)],[r.split()for r in open(INPUT_FILE).read().replace("addx","p\na").split("\n")],[1])[i-1]*i for i in[20,60,100,140,180,220])
part2 = sub(r"(.{40})",r"\1\n",''.join("#" if abs(x-c%40)<2 else "." for(c,x)in enumerate(reduce(lambda p,n:[*p,p[-1]+(int(n[1])if n[0]=="a" else 0)],[r.split()for r in INPUT_FILE.replace("addx","p\na").split("\n")],[1]))))

print(part1)
print(part2)
