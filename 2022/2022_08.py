"""Year 2022 Day 8.

By: David Leber
"""

from __future__ import annotations
from aocd.models import Puzzle, User
import numpy as np

year = 2022
day = 8

with open(f"{year}/session.txt", "r") as fh:
    token = fh.read().strip()

user = User(token=token)
puzzle = Puzzle(year=year, day=day, user=user)
data = puzzle.input_data.split("\n")
# data = """30373
# 25512
# 65332
# 33549
# 35390""".split(
#     "\n"
# )

pre_array = []
for line in data:
    pre_array.append([int(x) for x in line])

array = np.array(pre_array)

num_r, num_c = array.shape

# Iterating over the rows, the first
is_visible_above = []
is_visible_below = []
for r in range(0, num_r):
    cur_row = array[r, :]
    before_rows = array[:r, :]
    after_rows = array[(r + 1) :, :]

    if before_rows.shape[0] == 0:
        before_rows = -np.ones((1, num_c))
    if after_rows.shape[0] == 0:
        after_rows = -np.ones((1, num_c))

    # Figure out where we hit a new max
    is_visible_above.append(cur_row > before_rows.max(axis=0))
    is_visible_below.append(cur_row > after_rows.max(axis=0))

is_visible_above = np.array(is_visible_above)
is_visible_below = np.array(is_visible_below)

is_visible_left = []
is_visible_right = []
for c in range(0, num_c):
    cur_col = array[:, c]
    before_cols = array[:, :c]
    after_cols = array[:, (c + 1) :]

    if before_cols.shape[1] == 0:
        before_cols = -np.ones((num_r, 1))
    if after_cols.shape[1] == 0:
        after_cols = -np.ones((num_r, 1))

    # Figure out where we hit a new max
    is_visible_left.append(cur_col > before_cols.max(axis=1))
    is_visible_right.append(cur_col > after_cols.max(axis=1))

is_visible_left = np.array(is_visible_left).T
is_visible_right = np.array(is_visible_right).T

is_visible = np.logical_or.reduce(
    (
        is_visible_above,
        is_visible_below,
        is_visible_left,
        is_visible_right,
    )
)
num_visible = np.sum(is_visible)
puzzle.answer_a = num_visible

# Part B
scores = np.zeros((num_r, num_c))
for r in range(1, num_r - 1):
    for c in range(1, num_c - 1):
        cur_height = array[r, c]

        # Up
        up_array_to_look = np.flip(array[:r, c], axis=0)
        up_mask = up_array_to_look >= cur_height
        up_first_index = np.where(up_mask)[0]
        if len(up_first_index) > 0:
            up_factor = up_first_index[0] + 1
        else:
            up_factor = len(up_array_to_look)

        # Down
        down_array_to_look = array[(r + 1) :, c]
        down_mask = down_array_to_look >= cur_height
        down_first_index = np.where(down_mask)[0]
        if len(down_first_index) > 0:
            down_factor = down_first_index[0] + 1
        else:
            down_factor = len(down_array_to_look)

        # Left
        left_array_to_look = np.flip(array[r, :c], axis=0)
        left_mask = left_array_to_look >= cur_height
        left_first_index = np.where(left_mask)[0]
        if len(left_first_index) > 0:
            left_factor = left_first_index[0] + 1
        else:
            left_factor = len(left_array_to_look)

        # Right
        right_array_to_look = array[r, (c + 1) :]
        right_mask = right_array_to_look >= cur_height
        right_first_index = np.where(right_mask)[0]
        if len(right_first_index) > 0:
            right_factor = right_first_index[0] + 1
        else:
            right_factor = len(right_array_to_look)

        cur_score = up_factor * down_factor * left_factor * right_factor
        scores[r, c] = cur_score

puzzle.answer_b = int(np.max(scores))
