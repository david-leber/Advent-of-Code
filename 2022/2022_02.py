"""Year 2022 Day 2.

By: David Leber
"""

from aocd.models import Puzzle, User

year = 2022
day = 2

with open(f"{year}/session.txt", "r") as fh:
    token = fh.read()

user = User(token=token)
puzzle = Puzzle(year=year, day=day, user=user)
data = puzzle.input_data.split("\n")

# This is definitely hard coding, but in this case it's cleaner / faster at
# runtime than a bunch of if/else's.
scores_a = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

total_score = 0
for round in data:
    total_score += scores_a[round]

puzzle.answer_a = total_score

# Observation - we can just copy the combinations of pairs from above.
# They're the same games, just shuffled around.
scores_b = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}

total_score = 0
for round in data:
    total_score += scores_b[round]

puzzle.answer_b = total_score
print("here")
