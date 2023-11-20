from collections import deque

from abstract_application import AbstractApplication


class Uniq(AbstractApplication):

    name = "uniq"

    def __init__(self) -> None:
        super().__init__()

    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:
        ignore_case = '-i' in args
        file_name = None

        for arg in args:
            if arg != '-i':
                file_name = arg
                break

        lines = input
        if file_name:
            with open(file_name, 'r') as file:
                lines = file.readlines()

        last_line = None
        for line in lines:
            line_to_compare = line.lower() if ignore_case else line
            if line_to_compare != last_line:
                out.append(line)
                last_line = line_to_compare

# Add additional documentation or help messages as needed
