# ruff: noqa: E731


from functools import reduce


INPUT_FILE_TEST = "inputs/day07.test.in"
INPUT_FILE = "inputs/day07.in"


part1ol = lambda filename: [
    (rows := open(filename).read().split("\n")[:-1]),
    reduce(
        lambda prev, next: (
            "".join(
                "|"
                if (prev[0][i] in "|S" and next[i] == ".")
                or (i > 0 and prev[0][i - 1] in "|S" and next[i - 1] == "^")
                or (i < len(next) - 1 and prev[0][i + 1] in "|S" and next[i + 1] == "^")
                else "."
                for i in range(0, len(next))
            ),
            prev[1]
            + len(
                list(
                    filter(
                        lambda x: (x[0] == "|" and x[1] == "^"),
                        zip(prev[0], next),
                    )
                )
            ),
        ),
        rows[1:],
        (rows[0], 0),
    ),
][1][1]

print(part1ol(INPUT_FILE_TEST))
print(part1ol(INPUT_FILE))


part2ol = lambda filename: sum(
    [
        (rows := open(filename).read().split("\n")[:-1]),
        reduce(
            lambda p, n: reduce(
                lambda p1, n1: {
                    **p1,
                    **(
                        {
                            n1[0] - 1: n1[1] + p1.get(n1[0] - 1, 0),
                            n1[0] + 1: n1[1] + p1.get(n1[0] + 1, 0),
                        }
                        if n[n1[0]] == "^"
                        else {n1[0]: n1[1] + p1.get(n1[0], 0)}
                    ),
                },
                p.items(),
                {},
            ),
            rows[1:],
            {rows[0].index("S"): 1},
        ),
    ][1].values()
)

print(part2ol(INPUT_FILE_TEST))
print(part2ol(INPUT_FILE))
