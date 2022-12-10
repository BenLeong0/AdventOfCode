# INPUT_FILE = "inputs/day08test.in"
INPUT_FILE = "inputs/day08.in"

part1 = [sum(f[r][c]>min(max(f[r][:c]+" "),max(f[r][c+1:]+" "),max(list(zip(*f))[c][:r],default=" "),max(list(zip(*f))[c][r+1:],default=" "))for c in range(len(f[0]))for r in range(len(f)))for f in[open(INPUT_FILE).read().split("\n")]][0]
part2 = [max(g(f[r][c],f[r][:c][::-1])*g(f[r][c],f[r][c+1:])*g(f[r][c],list(zip(*f))[c][:r][::-1])*g(f[r][c],list(zip(*f))[c][r+1:])for g in[lambda n,l:l.index([x for x in l if x>=n][0])+1 if len([x for x in l if x>=n])>0 else len(l)]for r in range(len(f))for c in range(len(f[0])))for f in[open(INPUT_FILE).read().split("\n")]][0]

print(part1)
print(part2)
