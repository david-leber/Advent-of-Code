"""Year 2022 Day 8.

By: David Leber
"""

from __future__ import annotations
from aocd.models import Puzzle, User
import numpy as np

year = 2022
day = 9

with open(f"{year}/session.txt", "r") as fh:
    token = fh.read().strip()

user = User(token=token)
puzzle = Puzzle(year=year, day=day, user=user)
data = puzzle.input_data.split("\n")

delta_lookups = {
    "R": [0, 1],
    "L": [0, -1],
    "U": [-1, 0],
    "D": [1, 0],
}


def analyze_ropes(num_knots: int) -> int:
    positions = np.zeros((num_knots, 2))
    positions_visited = set()
    positions_visited.add(str(positions[-1, :]))

    for command in data:
        direction, distance = command.split(" ")

        cur_move = np.array(delta_lookups[direction])

        for _ in range(int(distance)):

            # Move the head
            positions[0, :] += cur_move

            # Pulls all the other knots behind it
            for knot_index in range(1, num_knots):
                lead_position = positions[knot_index - 1, :]
                follow_position = positions[knot_index, :]
                delta = lead_position - follow_position
                if np.any(np.abs(delta) > 1):
                    # Normalize the direction, account for zero division.
                    delta_norm = np.divide(
                        delta, np.abs(delta), where=delta != 0, out=np.array([0.0, 0.0])
                    )
                    positions[knot_index, :] += delta_norm
            positions_visited.add(str(positions[-1, :]))
    return len(positions_visited)


puzzle.answer_a = analyze_ropes(2)
puzzle.answer_b = analyze_ropes(10)
