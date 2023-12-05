from typing import List, Deque

from .application import Application


class Sort(Application):

    name = "sort"

    def __init__(self) -> None:
        super().__init__()

    def exec(self, args: List[str], input: List[str], out: Deque[str]) -> None:
        reverse_order = '-r' in args
        file_name = None

        for arg in args:
            if arg != '-r':
                file_name = arg
                break

        lines = input
        if file_name:
            with open(file_name, 'r') as file:
                lines = file.readlines()

        # Sorting the lines
        sorted_lines = sorted(lines, reverse=reverse_order)

        for line in sorted_lines:
            out.append(line)
