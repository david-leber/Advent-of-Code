"""Year 2022 Day 1.

By: David Leber
"""

from aocd.models import Puzzle, User
from queue import PriorityQueue

year = 2022
day = 1

with open(f"{year}/session.txt", "r") as fh:
    token = fh.read()

user = User(token=token)
puzzle = Puzzle(year=year, day=day, user=user)
data = puzzle.input_data.split("\n")


top_found = PriorityQueue()
running_total = 0

for i in data:
    if i != "":
        running_total += int(i)
    else:
        top_found.put(-running_total)
        running_total = 0

puzzle.answer_a = sum([-top_found.get() for _ in range(1)])
top_found.put(-int(puzzle.answer_a))
puzzle.answer_b = sum([-top_found.get() for _ in range(3)])
