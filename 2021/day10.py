import copy
from typing import List, Optional


test_input: List[str] = [
    r'[({(<(())[]>[[{[]{<()<>>',
    r'[(()[<>])]({[<{<<[]>>(',
    r'{([(<{}[<>[]}>{[]{[(<()>',
    r'(((({<>}<{<{<>}{[]{[]{}',
    r'[[<[([]))<([[{}[[()]]]',
    r'[{[{({}]{}}([{[{{{}}([]',
    r'{<[[]]>}<{[{[{[]{()[[[]',
    r'[<(<(<(<{}))><([]([]()',
    r'<{([([[(<>()){}]>(<<{{',
    r'<{([{{}}[<[[[<>{}]]]>[]]',
]

with open("input_files/day10.in", "r", newline="\n") as readfile:
    full_input = [line[:-1] for line in readfile.readlines()]


# Part 1

def find_syntax_error_score(lines: List[str]) -> int:
    pairings_and_scores = {
        ")": {"pair": "(", "score": 3},
        "]": {"pair": "[", "score": 57},
        "}": {"pair": "{", "score": 1197},
        ">": {"pair": "<", "score": 25137},
    }

    def get_corrupted_char_score(line: str) -> int:
        stack = []
        for char in line:
            if char not in pairings_and_scores:
                stack.append(char)
            elif len(stack) == 0 or stack[-1] != pairings_and_scores[char]["pair"]:
                return pairings_and_scores[char]["score"]   # Corrupted line
            else:
                stack.pop()
        return 0

    return sum([get_corrupted_char_score(line) for line in lines])

assert find_syntax_error_score(test_input) == 26397
print(find_syntax_error_score(full_input))


# Part 2

def find_closing_sequence_scores(lines: List[str]) -> int:
    pairings_and_scores = {
        "(": {"pair": ")", "score": 1},
        "[": {"pair": "]", "score": 2},
        "{": {"pair": "}", "score": 3},
        "<": {"pair": ">", "score": 4},
    }

    def get_line_score(line: str) -> Optional[int]:
        stack = []

        for char in line:
            if char in pairings_and_scores:
                stack.append(char)
            elif len(stack) == 0 or char != pairings_and_scores[stack[-1]]["pair"]:
                return None     # Corrupted line
            else:
                stack.pop()

        total_score = 0
        while stack:
            value = pairings_and_scores[stack.pop()]["score"]
            total_score = total_score * 5 + value
        return total_score

    filtered_scores = list(sorted(filter(lambda x: x is not None, map(get_line_score, lines))))
    return filtered_scores[len(filtered_scores)//2]

assert find_closing_sequence_scores(test_input) == 288957
print(find_closing_sequence_scores(full_input))
