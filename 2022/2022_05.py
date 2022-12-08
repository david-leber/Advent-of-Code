"""Year 2022 Day 5.

By: David Leber
"""

from aocd.models import Puzzle, User
import pandas as pd

year = 2022
day = 5

with open(f"{year}/session.txt", "r") as fh:
    token = fh.read()

user = User(token=token)
puzzle = Puzzle(year=year, day=day, user=user)
data = puzzle.input_data.split("\n")

# Parsing the starting position


def get_stacks(data: list[str]) -> tuple[list[list[str]], int]:
    stacks = []
    line_index = 0
    while data[line_index][0] == "[":
        stack_index = 0
        cur_line = data[line_index]
        while stack_index * 4 + 1 < len(cur_line):
            next_item = cur_line[stack_index * 4 + 1]

            # Needed because we don't know there are 10 stacks.
            if len(stacks) <= stack_index:
                stacks += [[]]
            if next_item != " ":
                stacks[stack_index] += [next_item]
            stack_index += 1
        line_index += 1
    return stacks, line_index + 2


# Part A
stacks, instructions_start_index = get_stacks(data)
for i in range(instructions_start_index, len(data)):
    cur_line = data[i]
    num_to_move, remainder = cur_line.split("move ")[1].split(" from ")
    from_stack_index, to_stack_index = remainder.split(" to ")
    num_to_move = int(num_to_move)
    from_stack_index = int(from_stack_index) - 1
    to_stack_index = int(to_stack_index) - 1

    for _ in range(num_to_move):
        stacks[to_stack_index] = [stacks[from_stack_index][0]] + stacks[to_stack_index]
        stacks[from_stack_index] = stacks[from_stack_index][1:]

puzzle.answer_a = "".join([x[0] for x in stacks])

# Part B
stacks, instructions_start_index = get_stacks(data)
for i in range(instructions_start_index, len(data)):
    cur_line = data[i]
    num_to_move, remainder = cur_line.split("move ")[1].split(" from ")
    from_stack_index, to_stack_index = remainder.split(" to ")
    num_to_move = int(num_to_move)
    from_stack_index = int(from_stack_index) - 1
    to_stack_index = int(to_stack_index) - 1

    stacks[to_stack_index] = (
        stacks[from_stack_index][0:num_to_move] + stacks[to_stack_index]
    )
    stacks[from_stack_index] = stacks[from_stack_index][num_to_move:]

puzzle.answer_b = "".join([x[0] for x in stacks])
