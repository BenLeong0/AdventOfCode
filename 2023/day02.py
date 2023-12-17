from utils import file_to_list


def part1(filename: str):
    rows = file_to_list(filename)
    possible_game_count = 0

    for game_id, game in enumerate(rows, start=1):
        red_max = green_max = blue_max = 0
        rounds = game.split(": ")[1].split("; ")
        for round in rounds:
            dice_pairs = [x.split(" ") for x in round.split(", ")]
            for pair in dice_pairs:
                if pair[1] == "red":
                    red_max = max(red_max, int(pair[0]))
                if pair[1] == "green":
                    green_max = max(green_max, int(pair[0]))
                if pair[1] == "blue":
                    blue_max = max(blue_max, int(pair[0]))

        if (
            red_max <= 12 and
            green_max <= 13 and
            blue_max <= 14
        ):
            possible_game_count += game_id

    return possible_game_count


def part2(filename: str):
    rows = file_to_list(filename)
    total_power = 0

    for game in rows:
        red_max = green_max = blue_max = 0
        rounds = game.split(": ")[1].split("; ")
        for round in rounds:
            dice_pairs = [x.split(" ") for x in round.split(", ")]
            for pair in dice_pairs:
                if pair[1] == "red":
                    red_max = max(red_max, int(pair[0]))
                if pair[1] == "green":
                    green_max = max(green_max, int(pair[0]))
                if pair[1] == "blue":
                    blue_max = max(blue_max, int(pair[0]))

        total_power += red_max * green_max * blue_max

    return total_power


if __name__ == "__main__":
    # res1 = part1("inputs/day02.test.in")
    res1 = part1("inputs/day02.in")
    print(res1)

    # res2 = part2("inputs/day02.test.in")
    res2 = part2("inputs/day02.in")
    print(res2)
