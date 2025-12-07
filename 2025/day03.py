# ruff: noqa: E731

from utils import file_to_list

INPUT_FILE_TEST = "inputs/day03.test.in"
INPUT_FILE = "inputs/day03.in"


def part1(filename: str) -> int:
    rows = file_to_list(filename)[0].split(",")

    sum = 0
    for row in rows:
        [lower, upper] = row.split("-")
        for i in range(int(lower), int(upper) + 1):
            stri = str(i)
            if stri[: len(stri) // 2] * 2 == stri:
                sum += i

    return sum


part1ol = lambda filename: sum(int(m1[1]+m2[1]) for row in open(filename).read().split("\n")[:-1] if (m1:=max(enumerate(row[:-1]),key=lambda r:r[1])) and (m2:=max(enumerate(row[m1[0]+1:]),key=lambda r:r[1])))

# print(part1(INPUT_FILE_TEST))
print(part1ol(INPUT_FILE_TEST))
# print(part1(INPUT_FILE))
print(part1ol(INPUT_FILE))

part2ol = lambda filename: sum(int(m1[1]+m2[1]+m3[1]+m4[1]+m5[1]+m6[1]+m7[1]+m8[1]+m9[1]+m10[1]+m11[1]+m12[1]) for row in open(filename).read().split("\n")[:-1] if (f:=lambda r:r[1]) and (e:=list(enumerate(row))) and (m1:=max(e[:-11],key=f)) and (m2:=max(e[m1[0]+1:-10],key=f)) and (m3:=max(e[m2[0]+1:-9],key=f)) and (m4:=max(e[m3[0]+1:-8],key=f)) and (m5:=max(e[m4[0]+1:-7],key=f)) and (m6:=max(e[m5[0]+1:-6],key=f)) and (m7:=max(e[m6[0]+1:-5],key=f)) and (m8:=max(e[m7[0]+1:-4],key=f)) and (m9:=max(e[m8[0]+1:-3],key=f)) and (m10:=max(e[m9[0]+1:-2],key=f)) and (m11:=max(e[m10[0]+1:-1],key=f)) and (m12:=max(e[m11[0]+1:],key=f)))

# print(part2(INPUT_FILE_TEST))
print(part2ol(INPUT_FILE_TEST))
# print(part2(INPUT_FILE))
print(part2ol(INPUT_FILE))
