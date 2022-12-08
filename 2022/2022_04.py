"""Year 2022 Day 4.

By: David Leber
"""

from aocd.models import Puzzle, User
import pandas as pd

year = 2022
day = 4

with open(f"{year}/session.txt", "r") as fh:
    token = fh.read()

user = User(token=token)
puzzle = Puzzle(year=year, day=day, user=user)
data = puzzle.input_data.split("\n")

series = pd.Series(data)
series.name = "combined"
separate = series.str.split("[,-]", expand=True)
separate = separate.astype(int)

a_min = separate[0]
a_max = separate[1]
b_min = separate[2]
b_max = separate[3]

# Part A
a_mask = ((b_min >= a_min) & (b_max <= a_max)) | ((b_min <= a_min) & (b_max >= a_max))
puzzle.answer_a = a_mask.sum()

# Part B
b_mask = (
    ((b_min <= a_max) & (b_min >= a_min))
    | ((b_max <= a_max) & (b_max >= a_min))
    | a_mask
)
puzzle.answer_b = b_mask.sum()
