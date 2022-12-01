"""Year 2022 Day 1

By: David Leber
"""

from aocd.models import Puzzle
from queue import PriorityQueue
puzzle = Puzzle(year=2022, day=1)
data = puzzle.input_data.split('\n')


top_found = PriorityQueue()
running_total = 0

for i in data:
    if i != "":
        running_total += int(i)
    else:
        top_found.put(running_total)
    
puzzle.answer_a = sum(top_found.queue[-1:])
puzzle.answer_a = sum(top_found.queue[-3:])