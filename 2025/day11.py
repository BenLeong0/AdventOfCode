# ruff:noqa:E731

INPUT_FILE_PART_1_TEST = "inputs/day11.1.test.in"
INPUT_FILE_PART_2_TEST = "inputs/day11.2.test.in"
INPUT_FILE = "inputs/day11.in"

part1ol = lambda filename: [e:={i:o.split(" ") for [i,o] in [x.split(": ") for x in open(filename).read().split("\n")[:-1]]},cache:={"out": 1},f:=lambda x="you":cache[x] if x in cache else sum(f(y) for y in e[x])][-1]()

print(part1ol(INPUT_FILE_PART_1_TEST))
print(part1ol(INPUT_FILE))

part2ol = lambda filename: [e:={i:o.split(" ") for [i,o] in [x.split(": ") for x in open(filename).read().split("\n")[:-1]]},ocache:={"out":1},dcache:={"dac":1,"out":0},fcache:={"fft":1,"out":0},(fft:=lambda x="svr":(x not in fcache and fcache.update({x:sum(fft(y) for y in e[x])})) or fcache[x])()*(dac:=lambda x="fft":(x not in dcache and dcache.update({x:sum(dac(y) for y in e[x])})) or dcache[x])()*(out:=lambda x="dac":(x not in ocache and ocache.update({x:sum(out(y) for y in e[x])})) or ocache[x])()][-1]

print(part2ol(INPUT_FILE_PART_2_TEST))
print(part2ol(INPUT_FILE))
