"""Year 2022 Day 7.

By: David Leber
"""

from __future__ import annotations
from aocd.models import Puzzle, User
from typing import Optional

year = 2022
day = 7

with open(f"{year}/session.txt", "r") as fh:
    token = fh.read().strip()

user = User(token=token)
puzzle = Puzzle(year=year, day=day, user=user)
data = puzzle.input_data.split("\n")


class Directory:
    def __init__(self, name: str, parent: Optional[Directory]) -> None:
        self.name = name
        self.path = "/" if parent is None else parent.path + name + "/"
        self.parent = parent
        self.size = 0
        if parent is not None:
            parent.add_child(self)
        self.children: list[Directory] = []

    def is_file(self):
        return len(self.children) == 0

    def is_dir(self):
        return not self.is_file()

    def add_child(self, child: Directory):
        self.children.append(child)
        self.add_size(child.size)

    def add_size(self, size: int):
        self.size += size
        if self.parent is not None:
            self.parent.add_size(size=size)


def pop_ls_output(data: list[str]) -> list[str]:
    output = []
    while len(data) > 0 and data[0][0] != "$":
        output.append(data.pop(0))
    return output


# Part A
data_iterator = data.copy()
cur_directory = Directory("/", parent=None)
found_directories: dict[str, Directory] = {cur_directory.path: cur_directory}
while len(data_iterator) > 0:
    command = data_iterator.pop(0)
    if command == "$ cd ..":
        cur_directory = cur_directory.parent
    elif command == "$ cd /":
        cur_directory = found_directories["/"]
    elif command[:4] == "$ cd":
        new_name = command.split("$ cd ")[1]
        new_directory = Directory(name=new_name, parent=cur_directory)
        if new_directory.path not in found_directories:
            found_directories[new_directory.path] = new_directory
        cur_directory = found_directories[new_directory.path]
    elif len(data_iterator) > 0:
        ls_output = pop_ls_output(data_iterator)
        for file in ls_output:
            size, filename = file.split(" ")
            if size.isnumeric():
                size = int(size)
                new_file = Directory(name=filename, parent=cur_directory)
                new_file.add_size(size)

puzzle.answer_a = sum(
    [
        found_directories[x].size
        for x in found_directories
        if found_directories[x].size <= 100_000 and found_directories[x].is_dir()
    ]
)

# Part B
total_space = 70000000
space_needed = 30000000
space_used = found_directories["/"].size
space_to_free = space_needed - (total_space - space_used)
smallest_found = total_space
for path in found_directories:
    cur_size = found_directories[path].size
    if cur_size >= space_to_free and cur_size < smallest_found:
        smallest_found = cur_size

puzzle.answer_b = smallest_found
