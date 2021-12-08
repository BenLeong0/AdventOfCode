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

with open("day8.in", "r", newline="\n") as readfile:
    full_input = [x[:-1] for x in readfile.readlines()]


# 2 lines => '1'
# 3 lines => '7'
# 4 lines => '4'
# 7 lines => '8'
# 6 lines, 2 overlap with '7' => '6'
# 5 lines, 5 overlap with '6' => '5'
# 5 lines, 2 overlap with '7' => '2'
# 5 lines, 3 overlap with '4' => '3'
# 6 lines, 5 overlap with '5' => '9'
# 6 lines, 4 overlap with '5' => '0'


# Part 1
def find_num_of_basic_letters(signals: List[str]) -> int:
    return sum([len([x for x in signal.split('|')[1].split() if len(x) in (2,3,4,7)]) for signal in signals])

assert find_num_of_basic_letters(test_input) == 26
print(find_num_of_basic_letters(full_input))


# Part 2
def find_sum_of_outputs(signals: List[str]) -> int:
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
        print(seen_letters)

        curr_sum += (
            1000 * seen_letters[''.join(sorted(output_signal[0]))] + 
            100 * seen_letters[''.join(sorted(output_signal[1]))] + 
            10 * seen_letters[''.join(sorted(output_signal[2]))] + 
            seen_letters[''.join(sorted(output_signal[3]))]
        )
    print('yo')
    return curr_sum

assert find_sum_of_outputs(test_input) == 61229
print(find_sum_of_outputs(full_input))
                
