from collections import deque

from applications.new_folder.abstract_application import AbstractApplication


class Sort(AbstractApplication):

    def exec(self, args: list[str], input: list[str], out: deque[str]) -> None:
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
