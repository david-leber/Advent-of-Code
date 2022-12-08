"""Year 2022 Day 6.

By: David Leber
"""

from aocd.models import Puzzle, User

year = 2022
day = 6

with open(f"{year}/session.txt", "r") as fh:
    token = fh.read().strip()

user = User(token=token)
puzzle = Puzzle(year=year, day=day, user=user)
data = puzzle.input_data


def find_code(data: str, stop_code_len: int) -> int:
    index = stop_code_len - 1
    while index < len(data):
        chars_found = set()
        found = True
        for test_offset in range(0, stop_code_len):
            test_char = data[index - test_offset]
            if test_char not in chars_found:
                chars_found.add(test_char)
            else:
                index += stop_code_len - test_offset  # Can skip ahead
                found = False
                break
        if found:
            break
    return index + 1


# Part A
stop_code_len = 4
puzzle.answer_a = find_code(data=data, stop_code_len=stop_code_len)

# Part B
stop_code_len = 14
puzzle.answer_b = find_code(data=data, stop_code_len=stop_code_len)
