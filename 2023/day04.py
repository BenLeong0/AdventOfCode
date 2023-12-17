import re

from utils import file_to_list

WHITESPACE_RE = re.compile(r" +")


def part1(filename: str):
    rows = file_to_list(filename)

    stripped_rows = [row.split(":")[1].split(" | ") for row in rows]
    winners_and_candidates = [
        (set(WHITESPACE_RE.split(row[0])[1:]), set(WHITESPACE_RE.split(row[1])))
        for row in stripped_rows
    ]
    print(winners_and_candidates)
    return sum(
        2 ** (num_winners - 1)
        for winners, candidates in winners_and_candidates
        if (num_winners := len(winners.intersection(candidates))) > 0
    )


def part2(filename: str):
    rows = file_to_list(filename)

    stripped_rows = [row.split(":")[1].split(" | ") for row in rows]
    winners_and_candidates = [
        (set(WHITESPACE_RE.split(row[0])[1:]), set(WHITESPACE_RE.split(row[1])))
        for row in stripped_rows
    ]
    card_counts = [1] * len(rows)
    for card_index, (winners, candidates) in enumerate(winners_and_candidates):
        num_wins = len(winners.intersection(candidates))
        for i in range(num_wins):
            card_counts[card_index + i + 1] += card_counts[card_index]

    print(card_counts)
    return sum(card_counts)


if __name__ == "__main__":
    # res1 = part1("inputs/day04.test.in")
    res1 = part1("inputs/day04.in")
    print(res1)

    # res2 = part2("inputs/day04.test.in")
    res2 = part2("inputs/day04.in")
    print(res2)
