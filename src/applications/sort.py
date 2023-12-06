import sys
from typing import Deque, List

from .application import Application, ApplicationError

class Sort(Application):
    name = 'sort'

    def exec(
        self,
        args: List[str],
        input: List[str],
        output: Deque[str]
    ) -> None:
        reverse = '-r' in args

        # Separate options from potential file path
        file_path = None
        for arg in args:
            if arg != '-r':
                file_path = arg
                break

        # Determine the source of data (file or stdin)
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
            except FileNotFoundError:
                raise ApplicationError(
                    f"{self.name}: {file_path}: Unable to read file."
                )
        else:
            # Use stdin if no file is specified
            lines = input

        sorted_lines = sorted(lines, reverse=reverse)
        formatted_output = ''.join(sorted_lines)
        output.append(formatted_output)
