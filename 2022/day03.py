from string import ascii_letters


# INPUT_FILE = "input/day03test.in"
INPUT_FILE = "input/day03.in"

part1 = sum(1+ascii_letters.index([c for c in x[:len(x)//2]if c in x[len(x)//2:]][0])for x in open(INPUT_FILE).read().split("\n"))
part2 = sum(1+ascii_letters.index(k)for k in [[[c for c in f[3*i]if c in f[3*i+1]and c in f[3*i+2]][0]for i in range(len(f)//3)]for f in [open(INPUT_FILE).read().split("\n")]][0])
# The `for f in [open(INPUT_FILE).read().split("\n")]][0]` is just to alias the file as `f`

print(part1)
print(part2)
