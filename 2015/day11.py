import re
from string import ascii_lowercase
from typing import List

NumbersPassword = List[int]


# Shared

def convert_from_letters_to_numbers(password: str) -> NumbersPassword:
    return [ascii_lowercase.index(char) for char in password]

def convert_from_numbers_to_letters(password: NumbersPassword) -> str:
    return ''.join([ascii_lowercase[idx] for idx in password])

def increment_password(password: NumbersPassword) -> None:
    for i in range(len(password)-1, -1, -1):
        if password[i] != 25:
            password[i] += 1
            return
        password[i] = 0


def is_valid_password(numbers_password: NumbersPassword) -> bool:
    letters_password = convert_from_numbers_to_letters(numbers_password)
    return (
        any([
            numbers_password[i] == numbers_password[i+1]-1  == numbers_password[i+2]-2
            for i in range(len(numbers_password) - 2)
        ]) and
        re.search(r"[ilo]", letters_password) is None and
        len(re.findall(r"(.)\1", letters_password)) >= 2
    )


def get_next_password(prev_password: str) -> str:
    numbers_password: NumbersPassword = convert_from_letters_to_numbers(prev_password)
    increment_password(numbers_password)
    while not is_valid_password(numbers_password):
        increment_password(numbers_password)
    return convert_from_numbers_to_letters(numbers_password)


assert get_next_password("abcdefgh") == "abcdffaa"
# assert get_next_password("ghijklmn") == "ghjaabcc"
print(get_next_password("vzbxkghb"))
print(get_next_password(get_next_password("vzbxkghb")))
