"""Year 2022 Day 3.

By: David Leber
"""

from aocd.models import Puzzle, User
import os

year = 2022
day = 3

with open(f"{year}/session.txt", "r") as fh:
    token = fh.read()

user = User(token=token)
puzzle = Puzzle(year=year, day=day, user=user)
data = puzzle.input_data.split("\n")


def get_score(letter: str) -> int:
    ascii_value = ord(letter)
    if ascii_value >= ord("a") and ascii_value <= ord("z"):
        return ascii_value - ord("a") + 1
    else:
        return ascii_value - ord("A") + 27


# Part A
score = 0
index = 0
for line in data:
    compartment_1 = line[: int(len(line) / 2)]
    compartment_2 = line[int(len(line) / 2) :]

    overlap = set(compartment_1).intersection(set(compartment_2)).pop()

    score += get_score(overlap)
puzzle.answer_a = score

# Part B
score = 0
index = 0
while index < len(data):
    batch1 = data[index]
    index += 1
    batch2 = data[index]
    index += 1
    batch3 = data[index]
    index += 1

    overlap = set(batch1).intersection(set(batch2)).intersection(batch3).pop()

    score += get_score(overlap)
puzzle.answer_b = score
