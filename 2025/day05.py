# ruff: noqa: E731


from functools import reduce


INPUT_FILE_TEST = "inputs/day05.test.in"
INPUT_FILE = "inputs/day05.in"


part1ol = lambda filename: [
    (rows := open(filename).read().split("\n")[:-1]),
    (i := rows.index("")),
    len(
        [
            0
            for id in rows[i + 1 :]
            if any(
                int((r := row.split("-"))[0]) <= int(id) <= int(r[1])
                for row in rows[:i]
            )
        ]
    ),
][2]

print(part1ol(INPUT_FILE_TEST))
print(part1ol(INPUT_FILE))


part2ol = lambda filename: reduce(
    lambda p, n: p + n[1] - n[0] + 1,
    reduce(
        lambda p, n: [
            *[x for x in p if not g(x, n)],
            reduce(
                lambda p1, n1: (min(p1[0], n1[0]), max(p1[1], n1[1])),
                [x for x in p if g(x, n)],
                n,
            ),
        ],
        map(
            lambda r: (int(r.split("-")[0]), int(r.split("-")[1])),
            (f := open(filename).read().split("\n"))[: f.index("")],
        ),
        []
        if (
            g := lambda x, y: x[0] <= y[0] <= x[1]
            or x[0] <= y[1] <= x[1]
            or y[0] <= x[0] <= y[1]
            or y[0] <= x[1] <= y[1]
        )
        else [],
    ),
    0,
)


print(part2ol(INPUT_FILE_TEST))
print(part2ol(INPUT_FILE))
