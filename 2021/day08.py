from typing import List


test_input: List[int] = [
    'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
    'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
    'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
    'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
    'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
    'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
    'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
    'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
    'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
    'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce',
]

with open("inputs/day08.in", "r", newline="\n") as readfile:
    full_input = [x[:-1] for x in readfile.readlines()]


# Part 1
def find_num_of_basic_letters(signals: List[str]) -> int:
    return sum([len([x for x in signal.split('|')[1].split() if len(x) in (2,3,4,7)]) for signal in signals])

assert find_num_of_basic_letters(test_input) == 26
print(find_num_of_basic_letters(full_input))


# Part 2
def combine_letters(letter1: str, letter2: str) -> str:
    # Imagine stacking the displays on top of each other (like bitwise OR)
    return ''.join(sorted(set(letter1+letter2)))


def find_sum_of_outputs(signals: List[str]) -> int:
    curr_sum = 0
    for signal in signals:
        letters = [''.join(sorted(x)) for x in signal.split()]
        codes = [''] * 10

        for letter in letters:
            if len(letter) == 2:
                codes[1] = letter
            elif len(letter) == 3:
                codes[7] = letter
            elif len(letter) == 4:
                codes[4] = letter
            elif len(letter) == 7:
                codes[8] = letter

        for letter in filter(lambda x: len(x) == 6, letters):
            if combine_letters(letter, codes[1]) == codes[8]:
                codes[6] = letter
            elif combine_letters(letter, codes[4]) == codes[8]:
                codes[0] = letter
            else:
                codes[9] = letter

        for letter in filter(lambda x: len(x) == 5, letters):
            if combine_letters(letter, codes[6]) == codes[6]:
                codes[5] = letter
            elif combine_letters(letter, codes[4]) == codes[8]:
                codes[2] = letter
            else:
                codes[3] = letter

        output_signal = [codes.index(''.join(sorted(x))) for x in signal.split('|')[1].split()]
        curr_sum += int(''.join(map(str, output_signal)))

    return curr_sum

assert find_sum_of_outputs(test_input) == 61229
print(find_sum_of_outputs(full_input))


######
# don't look please

def find_sum_of_outputs_DEAD(signals: List[str]) -> int:
    curr_sum = 0
    for signal in signals:
        letters = signal.split()

        seen_letters = {}

        for i in range(len(letters)):
            if len(letters[i]) == 2:
                seen_letters[''.join(sorted(letters.pop(i)))] = 1
                break

        for i in range(len(letters)):
            if len(letters[i]) == 3:
                seven = set(letters[i])
                seen_letters[''.join(sorted(letters.pop(i)))] = 7
                break

        for i in range(len(letters)):
            if len(letters[i]) == 4:
                four = set(letters[i])
                seen_letters[''.join(sorted(letters.pop(i)))] = 4
                break

        for i in range(len(letters)):
            if len(letters[i]) == 7:
                seen_letters[''.join(sorted(letters.pop(i)))] = 8
                break

        for i in range(len(letters)):
            if len(letters[i]) == 6 and len(seven.intersection(letters[i])) == 2:
                six = set(letters[i])
                seen_letters[''.join(sorted(letters.pop(i)))] = 6
                break

        for i in range(len(letters)):
            if len(letters[i]) == 5 and len(six.intersection(letters[i])) == 5:
                five = set(letters[i])
                seen_letters[''.join(sorted(letters.pop(i)))] = 5
                break

        for i in range(len(letters)):
            if len(letters[i]) == 5 and len(seven.intersection(letters[i])) == 2:
                seen_letters[''.join(sorted(letters.pop(i)))] = 2
                break

        for i in range(len(letters)):
            if len(letters[i]) == 5 and len(four.intersection(letters[i])) == 3:
                seen_letters[''.join(sorted(letters.pop(i)))] = 3
                break

        for i in range(len(letters)):
            if len(letters[i]) == 6 and len(five.intersection(letters[i])) == 4:
                seen_letters[''.join(sorted(letters.pop(i)))] = 0
                break

        for i in range(len(letters)):
            if len(letters[i]) == 6 and len(five.intersection(letters[i])) == 5:
                seen_letters[''.join(sorted(letters.pop(i)))] = 9
                break

        output_signal = signal.split('|')[1].split()

        curr_sum += (
            1000 * seen_letters[''.join(sorted(output_signal[0]))] +
            100 * seen_letters[''.join(sorted(output_signal[1]))] +
            10 * seen_letters[''.join(sorted(output_signal[2]))] +
            seen_letters[''.join(sorted(output_signal[3]))]
        )
    return curr_sum
