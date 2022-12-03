from string import ascii_letters


# INPUT_FILE = "inputs/day03test.in"
INPUT_FILE = "inputs/day03.in"

part1 = sum(1+ascii_letters.index([c for c in x[:len(x)//2]if c in x[len(x)//2:]][0])for x in open(INPUT_FILE).read().split("\n"))
part2 = sum(1+ascii_letters.index(k)for k in [[[c for c in f[i]if c in f[i+1]and c in f[i+2]][0]for i in range(0,len(f),3)]for f in [open(INPUT_FILE).read().split("\n")]][0])
# The `for f in [open(INPUT_FILE).read().split("\n")]][0]` is just to alias the file as `f`

print(part1)
print(part2)
