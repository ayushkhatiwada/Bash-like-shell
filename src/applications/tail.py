from typing import Deque, List
from collections import deque

from .application import Application, ApplicationError


class Tail(Application):
    name = "tail"

    def exec(self, args: List[str], input: List[str], out: Deque[str]) -> None:
        # Default number of lines to display
        num_lines = 10

        # Process command line arguments
        file_path = None
        for arg in args:
            if arg.startswith("-n"):
                try:
                    num_lines = int(arg[2:])
                except ValueError:
                    raise ApplicationError(
                        f"{self.name}: Invalid number of lines: {arg[2:]}"
                    )
            else:
                file_path = arg

        # Read from file or stdin
        try:
            if file_path:
                with open(file_path, "r") as file:
                    lines = file.readlines()
            else:
                lines = input
        except FileNotFoundError:
            raise ApplicationError(
                f"{self.name}: {file_path}: No such file or directory."
            )

        last_lines = deque(maxlen=num_lines)
        for line in lines:
            last_lines.append(line)

        formatted_output = "".join(last_lines)
        out.append(formatted_output)
